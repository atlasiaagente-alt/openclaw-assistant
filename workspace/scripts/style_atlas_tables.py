import json
import os
import urllib.request

TOKEN = os.environ.get('NOTION_TOKEN')
TABLES = {
    '3290a0b1-97cc-80c8-a64f-d3d8e47793c1': '⚙️ Trabajo / Operación',
    '3290a0b1-97cc-809a-b9aa-e84d03b4c898': '🚀 TradeLab / Producto',
    '3290a0b1-97cc-805a-ae65-f2f0f9981c2b': '🏠 Personal / Vida',
    '3290a0b1-97cc-80f4-98f8-cd4e17258a55': '🏋️ Entrenamiento',
    '3290a0b1-97cc-8072-8070-f11555f9db23': '❤️ Relación / Fechas'
}
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

def text(content):
    return {'type': 'text', 'text': {'content': content}}

def cell(content):
    if not content:
        return []
    return [text(content)]

def plain(cell_items):
    return ''.join(x.get('plain_text', '') for x in cell_items).strip()

def normalize_estado(value):
    v = value.strip().lower()
    mapping = {
        'pendiente': '🟡 Listo',
        'backlog': '📥 Inbox',
        'en progreso': '🔵 En progreso',
        'bloqueado': '⛔ Bloqueado',
        'en espera': '🕒 Waiting',
        'hecho': '✅ Hecho',
        'done': '✅ Hecho',
        'listo': '🟡 Listo',
        'definir': '🟣 Definir',
    }
    return mapping.get(v, value)

def normalize_prioridad(value):
    v = value.strip().lower()
    mapping = {
        'alta': '🔴 Alta',
        'media': '🟠 Media',
        'baja': '🟢 Baja',
    }
    return mapping.get(v, value)

for table_id in TABLES:
    rows = notion('GET', f'https://api.notion.com/v1/blocks/{table_id}/children?page_size=100')['results']
    if not rows:
        continue

    header = rows[0]
    width = len(header['table_row']['cells'])
    if width == 7:
        header_cells = [cell('Tarea'), cell('Estado'), cell('Tipo'), cell('Prioridad'), cell('Impacto'), cell('Área'), cell('Notas')]
    elif width == 6:
        header_cells = [cell('Tarea'), cell('Estado'), cell('Área'), cell('Prioridad'), cell('Fecha'), cell('Responsable')]
    elif width == 5 and table_id == '3290a0b1-97cc-80f4-98f8-cd4e17258a55':
        header_cells = [cell('Rutina'), cell('Tipo'), cell('Estado'), cell('Energía'), cell('Notas')]
    elif width == 5:
        header_cells = [cell('Item'), cell('Tipo'), cell('Fecha'), cell('Prioridad'), cell('Estado')]
    else:
        header_cells = header['table_row']['cells']

    notion('PATCH', f"https://api.notion.com/v1/blocks/{header['id']}", {'table_row': {'cells': header_cells}})

    for row in rows[1:]:
        cells = row['table_row']['cells']
        vals = [plain(c) for c in cells]

        if table_id == '3290a0b1-97cc-809a-b9aa-e84d03b4c898':
            vals[1] = normalize_estado(vals[1])
            vals[3] = normalize_prioridad(vals[3])
        elif table_id == '3290a0b1-97cc-80f4-98f8-cd4e17258a55':
            vals[2] = normalize_estado(vals[2])
            vals[3] = normalize_prioridad(vals[3])
        elif table_id == '3290a0b1-97cc-8072-8070-f11555f9db23':
            vals[3] = normalize_prioridad(vals[3])
            vals[4] = normalize_estado(vals[4])
        elif table_id == '3290a0b1-97cc-80c8-a64f-d3d8e47793c1':
            vals[1] = normalize_estado(vals[1])
            vals[3] = normalize_prioridad(vals[3])
        elif table_id == '3290a0b1-97cc-805a-ae65-f2f0f9981c2b':
            vals[1] = normalize_estado(vals[1])
            vals[3] = normalize_prioridad(vals[3])

        new_cells = [cell(v) for v in vals]
        notion('PATCH', f"https://api.notion.com/v1/blocks/{row['id']}", {'table_row': {'cells': new_cells}})

print('OK')
