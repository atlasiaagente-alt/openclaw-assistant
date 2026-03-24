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

def rt(text):
    return [{'type': 'text', 'text': {'content': text}}]

def append_children(parent_id, children, after=None):
    payload = {'children': children}
    if after:
        payload['after'] = after
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{parent_id}/children', payload)

# Insert visual titles before each table in reverse order so positions stay correct.
insertions = [
    ('3290a0b1-97cc-8072-8070-f11555f9db23', '❤️ Hestia · Relación / Fechas clave', 'Responsable principal: Hestia. Seguimiento de fechas, detalles y planes importantes.'),
    ('3290a0b1-97cc-80f4-98f8-cd4e17258a55', '🏋️ Ares · Entrenamiento / Disciplina', 'Responsable principal: Ares. Rutina, energía y consistencia semanal.'),
    ('3290a0b1-97cc-805a-ae65-f2f0f9981c2b', '🏠 Atlas · Personal / Vida', 'Responsable principal: Atlas. Pendientes personales, vida práctica y coordinación.'),
    ('3290a0b1-97cc-809a-b9aa-e84d03b4c898', '🚀 Prometeo · TradeLab / Producto', 'Responsable principal: Prometeo. MVP, prioridades técnicas y lanzamiento.'),
    ('3290a0b1-97cc-80c8-a64f-d3d8e47793c1', '⚡ Atlas · Operación / Sistema', 'Responsable principal: Atlas. Operación general, seguimiento y coordinación.'),
]

for table_id, title, subtitle in insertions:
    append_children(PAGE_ID, [
        {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': rt(title), 'color': 'default', 'is_toggleable': False}},
        {'object': 'block', 'type': 'paragraph', 'paragraph': {'rich_text': rt(subtitle), 'color': 'gray'}},
    ], after=table_id)

# Add training task to Ares table.
rows = notion('GET', 'https://api.notion.com/v1/blocks/3290a0b1-97cc-80f4-98f8-cd4e17258a55/children?page_size=100')['results']
existing = []
for row in rows[1:]:
    cells = row['table_row']['cells']
    name = ''.join(x.get('plain_text', '') for x in cells[0]).strip().lower()
    existing.append(name)

if 'pierna 5am manana' not in existing and 'pierna 5am mañana' not in existing:
    append_children('3290a0b1-97cc-80f4-98f8-cd4e17258a55', [
        {
            'object': 'block',
            'type': 'table_row',
            'table_row': {
                'cells': [
                    rt('Pierna 5AM mañana'),
                    rt('Pierna'),
                    rt('🟡 Listo'),
                    rt('🔴 Alta'),
                    rt('Recordar en Smart Project: mañana se entrena pierna a las 5:00 AM.')
                ]
            }
        }
    ])

print('OK')
