import json, os, urllib.request, urllib.error

TOKEN = os.environ['NOTION_TOKEN']
VERSION = '2025-09-03'
HEADERS = {
    'Authorization': 'Bearer ' + TOKEN,
    'Notion-Version': VERSION,
    'Content-Type': 'application/json',
}


def notion(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method=method, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}


def safe(label, fn):
    try:
        fn()
        print('ok', label)
    except urllib.error.HTTPError as e:
        body = ''
        try:
            body = e.read().decode('utf-8')
        except Exception:
            pass
        print('error', label, e.code, body[:250])
    except Exception as e:
        print('error', label, repr(e))


def text_cell(content):
    return [{"type": "text", "text": {"content": content}}]


def replace_row(row_id, cells):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{row_id}', {
        'table_row': {'cells': [text_cell(c) for c in cells]}
    })


# IDs obtenidos en el run anterior
prom_rows = [
    '3290a0b1-97cc-8043-be98-d02b7a9dff05',  # header
    '3290a0b1-97cc-8037-8aeb-e58c39cfded8',  # row1
    '3290a0b1-97cc-80f9-9c0f-fe9bf7933665',  # row2
    '3290a0b1-97cc-803f-a3ed-fc1a2d5d50ff',  # row3
    '32e0a0b1-97cc-814f-9ddb-f6d7f844458b',  # row4
]

# 7 cols: Tarea | Estado | Tipo | Prioridad | Impacto | Area | Notas
prom_data = [
    ('Validar pagos Paddle',   'Waiting',    'Payment',  'Alta',  'Alto',  'Payments',  'Unificar con "Validar Paddle webhook" o definir si son tareas separadas.'),
    ('Comprar dominio',        'Definir',    'Infra',    'Alta',  'Alto',  'Infra',     'Decidir dominio final y ejecutar compra.'),
    ('Ajustar UI dashboard',   'Definir',    'Feature',  'Media', 'Medio', 'Frontend',  'Concretar alcance minimo del ajuste visual.'),
    ('Validar Paddle webhook', 'En progreso','TradeLab', 'Alta',  'Alto',  'Payments',  'Prioridad 1. Revisar handler/ruta, firma/secreto y actualizacion del estado de pago.'),
]

for i, cells in enumerate(prom_data):
    rid = prom_rows[i + 1]
    safe(f'prom_row{i+1}', lambda r=rid, c=cells: replace_row(r, list(c)))

print('Prometeo fix completo.')
