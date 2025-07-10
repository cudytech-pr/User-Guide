import json

def filter_search_index(index_file):
    with open(index_file, 'r') as f:
        index = json.load(f)
    
    seen = set()
    filtered_index = []

    for entry in index:
        doc_id = entry['location']
        if doc_id not in seen:
            seen.add(doc_id)
            filtered_index.append(entry)
    
    with open(index_file, 'w') as f:
        json.dump(filtered_index, f, indent=4)

filter_search_index('filter_search_index.py')