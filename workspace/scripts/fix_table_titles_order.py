import json
import os
import urllib.request

TOKEN = os.environ.get('NOTION_TOKEN')
PAGE_ID = '3290a0b1-97cc-801a-8240-e78d3bfe0e74'
if not TOKEN:
    raise SystemExit('NOTION_TOKEN missing')

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

def notion(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method=method)
    for k, v in HEADERS.items():
        req.add_header(k, v)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

def plain_text(block):
    t = block['type']
    if t in ('heading_1','heading_2','heading_3','paragraph','bulleted_list_item','numbered_list_item','to_do','toggle','quote','callout'):
        payload = block[t]
        return ''.join(x.get('plain_text', '') for x in payload.get('rich_text', []))
    return ''

resp = notion('GET', f'https://api.notion.com/v1/blocks/{PAGE_ID}/children?page_size=100')
blocks = resp['results']

pairs = [
    ('⚡ Atlas · Operación / Sistema', 'Responsable principal: Atlas. Operación general, seguimiento y coordinación.', '3290a0b1-97cc-80c8-a64f-d3d8e47793c1'),
    ('🚀 Prometeo · TradeLab / Producto', 'Responsable principal: Prometeo. MVP, prioridades técnicas y lanzamiento.', '3290a0b1-97cc-809a-b9aa-e84d03b4c898'),
    ('🏠 Atlas · Personal / Vida', 'Responsable principal: Atlas. Pendientes personales, vida práctica y coordinación.', '3290a0b1-97cc-805a-ae65-f2f0f9981c2b'),
    ('🏋️ Ares · Entrenamiento / Disciplina', 'Responsable principal: Ares. Rutina, energía y consistencia semanal.', '3290a0b1-97cc-80f4-98f8-cd4e17258a55'),
    ('❤️ Hestia · Relación / Fechas clave', 'Responsable principal: Hestia. Seguimiento de fechas, detalles y planes importantes.', '3290a0b1-97cc-8072-8070-f11555f9db23'),
]

# archive misplaced title/subtitle blocks
for title, subtitle, _ in pairs:
    for block in blocks:
        txt = plain_text(block)
        if txt == title or txt == subtitle:
            notion('PATCH', f"https://api.notion.com/v1/blocks/{block['id']}", {'archived': True})

# refresh blocks after archive
blocks = notion('GET', f'https://api.notion.com/v1/blocks/{PAGE_ID}/children?page_size=100')['results']

# insert titles before each table by targeting the block before it
for title, subtitle, table_id in pairs:
    table_index = next(i for i, b in enumerate(blocks) if b['id'] == table_id)
    before_id = blocks[table_index - 1]['id'] if table_index > 0 else None
    children = [
        {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': [{'type': 'text', 'text': {'content': title}}], 'color': 'default', 'is_toggleable': False}},
        {'object': 'block', 'type': 'paragraph', 'paragraph': {'rich_text': [{'type': 'text', 'text': {'content': subtitle}}], 'color': 'gray'}},
    ]
    payload = {'children': children}
    if before_id:
        payload['after'] = before_id
    notion('PATCH', f'https://api.notion.com/v1/blocks/{PAGE_ID}/children', payload)
    blocks = notion('GET', f'https://api.notion.com/v1/blocks/{PAGE_ID}/children?page_size=100')['results']

print('OK')
