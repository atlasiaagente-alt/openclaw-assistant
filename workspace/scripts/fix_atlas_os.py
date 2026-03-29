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
        print('error', label, e.code, body[:200])
    except Exception as e:
        print('error', label, repr(e))


def rich_text(content):
    return [{"type": "text", "text": {"content": content}}]


def patch_heading(block_id, level, content):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {
        f'heading_{level}': {"rich_text": rich_text(content)}
    })


def text_cell(content):
    return [{"type": "text", "text": {"content": content}}]


def replace_row(row_id, cells):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{row_id}', {
        'table_row': {'cells': [text_cell(c) for c in cells]}
    })


def get_children(block_id):
    return notion('GET', f'https://api.notion.com/v1/blocks/{block_id}/children?page_size=100')


# --- Fix 1: headings that were heading_3 (update as heading_3, not paragraph) ---
ops = [
    ('hes_title h3',  lambda: patch_heading('32d0a0b1-97cc-8198-9166-e10da6999e69', 3, 'Hestia | Personal / Hogar')),
    ('ares_title h3', lambda: patch_heading('32d0a0b1-97cc-8162-8040-dfb1058545a3', 3, 'Ares | Entrenamiento / Disciplina')),
    ('rel_title h3',  lambda: patch_heading('32d0a0b1-97cc-8149-b08a-fa2133a57fcb', 3, 'Atlas | Relacion / Fechas clave')),
    ('sys_title h3',  lambda: patch_heading('32d0a0b1-97cc-815f-b40c-cf5b3509ec5d', 3, 'Atlas | Operacion / Sistema')),
]

# --- Fix 2: fetch actual row IDs for the 6-col Hestia table (id 3290a0b1-97cc-805a-ae65-f2f0f9981c2b) ---
# and the Ares table (id 3290a0b1-97cc-80f4-98f8-cd4e17258a55)
# to get current block IDs for the data rows

print('--- Fetching Hestia table rows ---')
hestia_tbl = get_children('3290a0b1-97cc-805a-ae65-f2f0f9981c2b')
hestia_rows = [(b['id'], b['type']) for b in hestia_tbl.get('results', [])]
for i, (rid, rtype) in enumerate(hestia_rows):
    print(f'  row{i}: {rid} ({rtype})')

print('--- Fetching Ares table rows ---')
ares_tbl = get_children('3290a0b1-97cc-80f4-98f8-cd4e17258a55')
ares_rows = [(b['id'], b['type']) for b in ares_tbl.get('results', [])]
for i, (rid, rtype) in enumerate(ares_rows):
    print(f'  row{i}: {rid} ({rtype})')

print('--- Fetching Atlas|Relacion table rows ---')
rel_tbl = get_children('3290a0b1-97cc-8072-8070-f11555f9db23')
rel_rows = [(b['id'], b['type']) for b in rel_tbl.get('results', [])]
for i, (rid, rtype) in enumerate(rel_rows):
    print(f'  row{i}: {rid} ({rtype})')

print('--- Fetching Atlas|Sistema table rows ---')
sys_tbl = get_children('32e0a0b1-97cc-81aa-8735-c8fde94a15a4')
sys_rows = [(b['id'], b['type']) for b in sys_tbl.get('results', [])]
for i, (rid, rtype) in enumerate(sys_rows):
    print(f'  row{i}: {rid} ({rtype})')

# Apply heading fixes
for label, fn in ops:
    safe(label, fn)

# Now patch Hestia rows (6 cols: Tarea | Estado | Area | Prioridad | Fecha | Responsable)
# row0 = header, skip
hestia_data = [
    ('Limpiar oficinas',      'Listo',         'Jorge',    'Alta',  'Limpieza', 'Mariela'),
    ('Comprar mercado',       'Pendiente hoy', 'Gustavo',  'Media', 'Hogar',    'Hestia: revisar faltantes y cerrar lista hoy'),
    ('Preparar desayuno',     'Listo',         'Jorge',    'Media', 'Desayuno', 'Mariela'),
    ('Lavar ropa sin mezclar','Listo',         'Jorge',    'Alta',  'Ropa',     'Mariela'),
    ('Comprar agua segun tablero','Waiting',   'Hogar',    'Media', '',         'Esperando confirmacion de Jorge'),
]
for i, cells in enumerate(hestia_data):
    if i + 1 < len(hestia_rows):
        rid = hestia_rows[i + 1][0]
        safe(f'hestia_row{i+1}', lambda r=rid, c=cells: replace_row(r, list(c)))

# Ares rows (5 cols: Rutina | Tipo | Estado | Energia | Notas)
ares_data = [
    ('Torso A',   'Torso',    'Listo',    'Media',    ''),
    ('Pierna A',  'Pierna',   'Listo',    'Alta',     ''),
    ('Descanso',  'Descanso', 'Listo',    'Baja',     ''),
    ('Entrenamiento de pecho manana 5AM 26/abril/2026','Bloqueado','Bloqueado','Media','Fecha inconsistente. Corregir antes de ejecutar cualquier aviso.'),
    ('Pedir fotos para el grupo de smart project','Bloqueado','Bloqueado','Media','Falta definir quien envia y en que canal exacto.'),
]
for i, cells in enumerate(ares_data):
    if i + 1 < len(ares_rows):
        rid = ares_rows[i + 1][0]
        safe(f'ares_row{i+1}', lambda r=rid, c=cells: replace_row(r, list(c)))

# Atlas|Relacion rows (5 cols: Item | Tipo | Fecha | Prioridad | Estado)
rel_data = [
    ('Cumpleanos novia', 'Fecha especial', '01/09/2026', 'Alta', 'Listo'),
    ('Cena especial',    'Plan',           'Definir',    'Media', 'Listo'),
    ('Comprar flores',   'Regalo',         'Definir',    'Alta',  'Listo'),
]
for i, cells in enumerate(rel_data):
    if i + 1 < len(rel_rows):
        rid = rel_rows[i + 1][0]
        safe(f'rel_row{i+1}', lambda r=rid, c=cells: replace_row(r, list(c)))

# Atlas|Sistema rows (7 cols: Tarea | Estado | Tipo | Prioridad | Impacto | Area | Notas)
sys_data = [
    ('Ideas de viaje para la siguiente semana','Definir','Vida practica','Alta','Medio','Viaje','Definir rango, presupuesto y compania; proponer 3-5 opciones concretas.'),
    ('Mejorar proactividad de OpenClaw','Definir','Sistema','Alta','Alto','Sistema','Convertir en plan operativo corto: triggers, rutina y seguimiento.'),
]
for i, cells in enumerate(sys_data):
    if i + 1 < len(sys_rows):
        rid = sys_rows[i + 1][0]
        safe(f'sys_row{i+1}', lambda r=rid, c=cells: replace_row(r, list(c)))

print('Fix completo.')
