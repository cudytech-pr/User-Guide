// index-docs.mjs
// 运行方式: node index-docs.mjs

import fs from "fs";
import path from "path";
import { execSync } from "child_process";

// ── 配置 ──────────────────────────────────────────────────────────────────────
const ACCOUNT_ID = "d09f25080af59e8d7e71f32ee78ecd05";
const API_TOKEN  = "cfut_q4R9bv1QB3NAlC4waA1h8C9JNEPsh3M4Y8zCob1R6ef6ae92";
const DOCS_DIR   = "./docs";
const CHUNK_SIZE = 800;
const CHUNK_OVERLAP = 100;
const BATCH_SIZE = 50;
const INDEX_NAME = "cudy-docs";

// ── 工具函数 ──────────────────────────────────────────────────────────────────

function getMdFiles(dir) {
  let files = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files = files.concat(getMdFiles(fullPath));
    } else if (entry.name.endsWith(".md")) {
      files.push(fullPath);
    }
  }
  return files;
}

function cleanMarkdown(text) {
  return text
    .replace(/^---[\s\S]*?---/m, "")
    .replace(/```[\s\S]*?```/g, "")
    .replace(/`[^`]+`/g, "")
    .replace(/!\[.*?\]\(.*?\)/g, "")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/#{1,6}\s/g, "")
    .replace(/\*\*([^*]+)\*\*/g, "$1")
    .replace(/\*([^*]+)\*/g, "$1")
    .replace(/^\s*[-*+]\s/gm, "")
    .replace(/^\s*\d+\.\s/gm, "")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function chunkText(text, chunkSize, overlap) {
  const chunks = [];
  let start = 0;
  while (start < text.length) {
    const end = Math.min(start + chunkSize, text.length);
    const chunk = text.slice(start, end).trim();
    if (chunk.length > 50) chunks.push(chunk);
    start += chunkSize - overlap;
  }
  return chunks;
}

async function getEmbeddings(texts) {
  const url = `https://api.cloudflare.com/client/v4/accounts/${ACCOUNT_ID}/ai/run/@cf/baai/bge-base-en-v1.5`;
  const res = await fetch(url, {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${API_TOKEN}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: texts }),
  });
  const data = await res.json();
  if (!data.success) {
    console.error("Embedding API error:", JSON.stringify(data.errors));
    return null;
  }
  return data.result?.data || null;
}

function upsertVectors(vectors) {
  const ndjson = vectors.map(v => JSON.stringify(v)).join("\n");
  const tmpFile = "./_tmp_vectors.ndjson";
  fs.writeFileSync(tmpFile, ndjson, "utf8");
  try {
    execSync(`wrangler vectorize insert ${INDEX_NAME} --file=${tmpFile}`, {
      encoding: "utf8",
      stdio: "pipe",
    });
  } finally {
    if (fs.existsSync(tmpFile)) fs.unlinkSync(tmpFile);
  }
}

function makeId(str) {
  return Buffer.from(str).toString("base64")
    .replace(/[^a-zA-Z0-9_-]/g, "")
    .slice(0, 64);
}

async function main() {
  console.log("📂 扫描文档目录...");
  const files = getMdFiles(DOCS_DIR);
  console.log(`✅ 找到 ${files.length} 个 Markdown 文件\n`);

  let allChunks = [];
  for (const file of files) {
    const raw = fs.readFileSync(file, "utf8");
    const clean = cleanMarkdown(raw);
    if (!clean) continue;
    const relativePath = path.relative(".", file).replace(/\\/g, "/");
    const chunks = chunkText(clean, CHUNK_SIZE, CHUNK_OVERLAP);
    chunks.forEach((chunk, i) => {
      allChunks.push({ id: `${relativePath}::${i}`, text: chunk, source: relativePath });
    });
  }

  console.log(`📝 共切割出 ${allChunks.length} 个段落\n`);

  let uploaded = 0;
  for (let i = 0; i < allChunks.length; i += BATCH_SIZE) {
    const batch = allChunks.slice(i, i + BATCH_SIZE);
    const texts = batch.map(c => c.text);
    const total = allChunks.length;
    process.stdout.write(`⚙️  处理 ${i + 1}~${Math.min(i + BATCH_SIZE, total)} / ${total}...`);

    const embeddings = await getEmbeddings(texts);
    if (!embeddings || embeddings.length !== batch.length) {
      console.log(" ❌ 向量生成失败，跳过");
      continue;
    }

    const vectors = batch.map((chunk, idx) => ({
      id: makeId(chunk.id),
      values: embeddings[idx],
      metadata: {
        text: chunk.text.slice(0, 1000),
        source: chunk.source,
      },
    }));

    try {
      upsertVectors(vectors);
      uploaded += vectors.length;
      console.log(" ✅");
    } catch (e) {
      console.log(" ❌ 上传失败:", e.message);
    }

    await new Promise(r => setTimeout(r, 300));
  }

  console.log(`\n🎉 完成！共上传 ${uploaded} 个向量到索引 "${INDEX_NAME}"`);
}

main().catch(console.error);
