(function () {
  const WORKER_URL = "https://cudydocs.maggie-chen-d09.workers.dev";

  const UI_TEXT = {
    en: {
      title: "Cudy Support",
      subtitle: "Ask me anything about Cudy products",
      placeholder: "Type your question...",
      send: "Send",
      welcome: "👋 Hi! I'm Cudy's AI assistant. Ask me about routers, switches, or any Cudy product!",
      lang: "中文",
      error: "Sorry, something went wrong. Please try again.",
      contactBtn: "📧 Contact Support",
      contactTitle: "Contact Support",
      contactBack: "← Back to Chat",
      contactName: "Your Name",
      contactEmail: "Your Email",
      contactMessage: "Describe your issue...",
      contactSend: "Send Message",
      contactSending: "Sending...",
      contactSuccess: "✅ Message sent! We'll get back to you at your email.",
      contactError: "❌ Failed to send. Please email support@cudy.com directly.",
      contactNameRequired: "Please enter your name.",
      contactEmailRequired: "Please enter a valid email.",
      contactMessageRequired: "Please describe your issue.",
    },
    zh: {
      title: "Cudy 智能客服",
      subtitle: "询问任何关于 Cudy 产品的问题",
      placeholder: "输入你的问题...",
      send: "发送",
      welcome: "👋 你好！我是 Cudy 的 AI 助手，可以解答路由器、交换机等产品相关问题！",
      lang: "English",
      error: "抱歉，出现了一些问题，请稍后重试。",
      contactBtn: "📧 联系客服",
      contactTitle: "联系客服",
      contactBack: "← 返回对话",
      contactName: "你的姓名",
      contactEmail: "你的邮箱",
      contactMessage: "请描述你的问题...",
      contactSend: "发送消息",
      contactSending: "发送中...",
      contactSuccess: "✅ 消息已发送！我们会尽快回复你的邮箱。",
      contactError: "❌ 发送失败，请直接发邮件至 support@cudy.com",
      contactNameRequired: "请输入你的姓名。",
      contactEmailRequired: "请输入有效的邮箱地址。",
      contactMessageRequired: "请描述你的问题。",
    },
  };

  let lang = "en";
  let isOpen = false;
  let isLoading = false;
  let isContactView = false;
  let history = [];

  const root = document.createElement("div");
  root.id = "cudy-chatbot-root";
  document.body.appendChild(root);

  root.innerHTML = `
    <button id="cudy-fab" aria-label="Open support chat">
      <span class="cudy-fab-icon cudy-icon-chat">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
        </svg>
      </span>
      <span class="cudy-fab-icon cudy-icon-close" style="display:none">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
          <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
        </svg>
      </span>
    </button>

    <div id="cudy-panel" class="cudy-panel-closed">
      <div id="cudy-header">
        <div class="cudy-header-left">
          <div class="cudy-avatar">
            <img src="https://docs.cudy.com/images/cudyicon.webp" alt="Cudy" onerror="this.style.display='none'"/>
          </div>
          <div>
            <div id="cudy-title"></div>
            <div id="cudy-subtitle"></div>
          </div>
        </div>
        <button id="cudy-lang-btn"></button>
      </div>

      <!-- 聊天视图 -->
      <div id="cudy-chat-view">
        <div id="cudy-messages"></div>
        <div id="cudy-contact-bar">
          <button id="cudy-contact-btn"></button>
        </div>
        <div id="cudy-input-area">
          <textarea id="cudy-input" rows="1" autocomplete="off" autocorrect="off"></textarea>
          <button id="cudy-send-btn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
            </svg>
          </button>
        </div>
      </div>

      <!-- 联系表单视图 -->
      <div id="cudy-contact-view" style="display:none">
        <div id="cudy-contact-form">
          <button id="cudy-back-btn"></button>
          <div class="cudy-field">
            <input id="cudy-name" type="text" autocomplete="name"/>
          </div>
          <div class="cudy-field">
            <input id="cudy-email" type="email" autocomplete="email"/>
          </div>
          <div class="cudy-field">
            <textarea id="cudy-msg" rows="5"></textarea>
          </div>
          <div id="cudy-form-feedback"></div>
          <button id="cudy-form-send-btn"></button>
        </div>
      </div>
    </div>
  `;

  // ── REFS ──────────────────────────────────────────────────────────────────
  const fab = document.getElementById("cudy-fab");
  const panel = document.getElementById("cudy-panel");
  const messagesEl = document.getElementById("cudy-messages");
  const inputEl = document.getElementById("cudy-input");
  const sendBtn = document.getElementById("cudy-send-btn");
  const langBtn = document.getElementById("cudy-lang-btn");
  const titleEl = document.getElementById("cudy-title");
  const subtitleEl = document.getElementById("cudy-subtitle");
  const contactBtn = document.getElementById("cudy-contact-btn");
  const chatView = document.getElementById("cudy-chat-view");
  const contactView = document.getElementById("cudy-contact-view");
  const backBtn = document.getElementById("cudy-back-btn");
  const nameInput = document.getElementById("cudy-name");
  const emailInput = document.getElementById("cudy-email");
  const msgInput = document.getElementById("cudy-msg");
  const formFeedback = document.getElementById("cudy-form-feedback");
  const formSendBtn = document.getElementById("cudy-form-send-btn");

  function t(key) { return UI_TEXT[lang][key]; }

  function updateUIText() {
    titleEl.textContent = isContactView ? t("contactTitle") : t("title");
    subtitleEl.textContent = isContactView ? "" : t("subtitle");
    inputEl.placeholder = t("placeholder");
    sendBtn.title = t("send");
    langBtn.textContent = t("lang");
    contactBtn.textContent = t("contactBtn");
    backBtn.textContent = t("contactBack");
    nameInput.placeholder = t("contactName");
    emailInput.placeholder = t("contactEmail");
    msgInput.placeholder = t("contactMessage");
    formSendBtn.textContent = t("contactSend");
  }

  function appendMessage(role, text, isTemp = false) {
    const wrap = document.createElement("div");
    wrap.className = `cudy-msg cudy-msg-${role}${isTemp ? " cudy-msg-temp" : ""}`;
    const bubble = document.createElement("div");
    bubble.className = "cudy-bubble";
    if (isTemp) {
      bubble.innerHTML = `<span class="cudy-dots"><span></span><span></span><span></span></span>`;
    } else {
      bubble.innerHTML = text
        .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/`(.*?)`/g, "<code>$1</code>")
        .replace(/\n/g, "<br>");
    }
    wrap.appendChild(bubble);
    messagesEl.appendChild(wrap);
    messagesEl.scrollTop = messagesEl.scrollHeight;
    return wrap;
  }

  function removeTemp() {
    const el = messagesEl.querySelector(".cudy-msg-temp");
    if (el) el.remove();
  }

  function showContactView(show) {
    isContactView = show;
    chatView.style.display = show ? "none" : "flex";
    contactView.style.display = show ? "flex" : "none";
    formFeedback.textContent = "";
    formFeedback.className = "";
    updateUIText();
  }

  // ── TOGGLE ────────────────────────────────────────────────────────────────
  fab.addEventListener("click", () => {
    isOpen = !isOpen;
    panel.className = isOpen ? "cudy-panel-open" : "cudy-panel-closed";
    fab.querySelector(".cudy-icon-chat").style.display = isOpen ? "none" : "flex";
    fab.querySelector(".cudy-icon-close").style.display = isOpen ? "flex" : "none";
    if (isOpen && messagesEl.children.length === 0) appendMessage("bot", t("welcome"));
    if (isOpen) setTimeout(() => inputEl.focus(), 300);
  });

  // ── LANGUAGE ──────────────────────────────────────────────────────────────
  langBtn.addEventListener("click", () => {
    lang = lang === "en" ? "zh" : "en";
    history = [];
    messagesEl.innerHTML = "";
    showContactView(false);
    updateUIText();
    appendMessage("bot", t("welcome"));
  });

  // ── CONTACT VIEW ──────────────────────────────────────────────────────────
  contactBtn.addEventListener("click", () => showContactView(true));
  backBtn.addEventListener("click", () => showContactView(false));

  formSendBtn.addEventListener("click", async () => {
    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const message = msgInput.value.trim();

    formFeedback.textContent = "";
    if (!name) { formFeedback.textContent = t("contactNameRequired"); formFeedback.className = "cudy-feedback-error"; return; }
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { formFeedback.textContent = t("contactEmailRequired"); formFeedback.className = "cudy-feedback-error"; return; }
    if (!message) { formFeedback.textContent = t("contactMessageRequired"); formFeedback.className = "cudy-feedback-error"; return; }

    formSendBtn.disabled = true;
    formSendBtn.textContent = t("contactSending");

    try {
      const res = await fetch(WORKER_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: "contact", name, email, message, lang }),
      });
      const data = await res.json();
      if (!res.ok || !data.success) throw new Error();
      formFeedback.textContent = t("contactSuccess");
      formFeedback.className = "cudy-feedback-success";
      nameInput.value = "";
      emailInput.value = "";
      msgInput.value = "";
    } catch {
      formFeedback.textContent = t("contactError");
      formFeedback.className = "cudy-feedback-error";
    }

    formSendBtn.disabled = false;
    formSendBtn.textContent = t("contactSend");
  });

  // ── SEND CHAT MESSAGE ─────────────────────────────────────────────────────
  async function sendMessage() {
    const text = inputEl.value.trim();
    if (!text || isLoading) return;

    inputEl.value = "";
    inputEl.style.height = "auto";
    isLoading = true;
    sendBtn.disabled = true;

    appendMessage("user", text);
    history.push({ role: "user", content: text });
    appendMessage("bot", "", true);

    try {
      const res = await fetch(WORKER_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: history, lang, source: window.location.pathname }),
      });
      const data = await res.json();
      if (!res.ok || data.error) throw new Error(data.error || "Unknown error");
      const reply = data.reply || t("error");
      removeTemp();
      appendMessage("bot", reply);
      history.push({ role: "assistant", content: reply });
    } catch (e) {
      console.error("Cudy chatbot error:", e);
      removeTemp();
      appendMessage("bot", t("error"));
    }

    isLoading = false;
    sendBtn.disabled = false;
    inputEl.focus();
  }

  sendBtn.addEventListener("click", sendMessage);
  inputEl.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); sendMessage(); }
  });
  inputEl.addEventListener("input", () => {
    inputEl.style.height = "auto";
    inputEl.style.height = Math.min(inputEl.scrollHeight, 120) + "px";
  });

  updateUIText();
})();