import json
import os
import sys
import urllib.parse
import urllib.request

TOKEN = os.environ.get('NOTION_TOKEN')
if not TOKEN:
    raise SystemExit('NOTION_TOKEN missing')

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Notion-Version': '2025-09-03',
    'Content-Type': 'application/json',
}


def notion(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method=method, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))


def rich_text_plain(rt):
    if not rt:
        return ''
    out = []
    for item in rt:
        t = item.get('plain_text')
        if t:
            out.append(t)
    return ''.join(out).strip()


def title_from_properties(props):
    for value in props.values():
        if value.get('type') == 'title':
            return rich_text_plain(value.get('title', []))
    return ''


def prop_plain(prop):
    if not prop:
        return None
    t = prop.get('type')
    if t == 'title':
        return rich_text_plain(prop.get('title', []))
    if t == 'rich_text':
        return rich_text_plain(prop.get('rich_text', []))
    if t == 'status':
        s = prop.get('status') or {}
        return s.get('name')
    if t == 'select':
        s = prop.get('select') or {}
        return s.get('name')
    if t == 'multi_select':
        return [x.get('name') for x in prop.get('multi_select', [])]
    if t == 'people':
        return [x.get('name') for x in prop.get('people', [])]
    if t == 'checkbox':
        return prop.get('checkbox')
    if t == 'url':
        return prop.get('url')
    if t == 'email':
        return prop.get('email')
    if t == 'phone_number':
        return prop.get('phone_number')
    if t == 'number':
        return prop.get('number')
    if t == 'date':
        d = prop.get('date') or {}
        return d.get('start')
    if t == 'formula':
        f = prop.get('formula') or {}
        return f.get(f.get('type'))
    if t == 'relation':
        return [x.get('id') for x in prop.get('relation', [])]
    return None


def page_summary(page):
    props = page.get('properties', {})
    data = {k: prop_plain(v) for k, v in props.items()}
    data['__title'] = title_from_properties(props)
    data['__url'] = page.get('url')
    return data


query = sys.argv[1] if len(sys.argv) > 1 else 'Atlas OS'
search = notion('POST', 'https://api.notion.com/v1/search', {'query': query})
pages = [r for r in search.get('results', []) if r.get('object') == 'page']
page = None
for p in pages:
    if title_from_properties(p.get('properties', {})) == 'Atlas OS':
        page = p
        break
if not page and pages:
    page = pages[0]
if not page:
    raise SystemExit('Atlas OS page not found')

page_id = page['id']
children = notion('GET', f'https://api.notion.com/v1/blocks/{page_id}/children?page_size=100')
blocks = children.get('results', [])

out = {
    'page_id': page_id,
    'page_url': page.get('url'),
    'child_blocks': [],
    'data_sources': [],
    'page_items': []
}

for b in blocks:
    item = {
        'id': b.get('id'),
        'type': b.get('type'),
        'has_children': b.get('has_children', False),
        'data_source': (b.get('data_source') or {}).get('id'),
        'link_to_page': (b.get('link_to_page') or {}).get('page_id') or (b.get('link_to_page') or {}).get('data_source_id'),
        'child_database': (b.get('child_database') or {}).get('title'),
        'text': rich_text_plain((b.get(b.get('type'), {}) or {}).get('rich_text', []))
    }
    if b.get('type') == 'child_page':
        cp = notion('GET', f"https://api.notion.com/v1/pages/{b.get('id')}")
        item['title'] = title_from_properties(cp.get('properties', {}))
    elif b.get('type') == 'table':
        rows = notion('GET', f"https://api.notion.com/v1/blocks/{b.get('id')}/children?page_size=100").get('results', [])
        table_rows = []
        for r in rows:
            if r.get('type') == 'table_row':
                cells = []
                for cell in (r.get('table_row') or {}).get('cells', []):
                    cells.append(rich_text_plain(cell))
                table_rows.append(cells)
        item['rows'] = table_rows
    out['child_blocks'].append(item)

seen = set()
for b in blocks:
    bid = b.get('id')
    btype = b.get('type')
    if btype == 'data_source':
        dsid = (b.get('data_source') or {}).get('id')
        if dsid and dsid not in seen:
            seen.add(dsid)
            q = notion('POST', f'https://api.notion.com/v1/data_sources/{dsid}/query', {'page_size': 100})
            out['data_sources'].append({
                'id': dsid,
                'title': rich_text_plain((b.get('data_source') or {}).get('title', [])),
                'items': [page_summary(x) for x in q.get('results', []) if x.get('object') == 'page']
            })
    elif btype == 'child_database':
        title = (b.get('child_database') or {}).get('title')
        # child_database id equals block id in older API patterns; attempt query via databases endpoint unsupported in 2025-09-03.
        out['page_items'].append({'child_database_title': title, 'id': bid})

print(json.dumps(out, ensure_ascii=True, indent=2))
