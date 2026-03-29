import json, os, sys, urllib.request, urllib.error
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TOKEN = os.environ['NOTION_TOKEN']
VERSION = '2025-09-03'
PAGE_ID = '3290a0b1-97cc-801a-8240-e78d3bfe0e74'
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
        result = fn()
        print('ok', label)
        return result
    except urllib.error.HTTPError as e:
        body = ''
        try:
            body = e.read().decode('utf-8')
        except Exception:
            pass
        print('error', label, e.code, body[:250])
    except Exception as e:
        print('error', label, repr(e))


def rich_text(content):
    return [{"type": "text", "text": {"content": content}}]


def text_cell(content):
    return [{"type": "text", "text": {"content": content}}]


def get_children(block_id):
    return notion('GET', f'https://api.notion.com/v1/blocks/{block_id}/children?page_size=100')


def append_children(block_id, children):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}/children', {
        'children': children
    })


def make_heading(level, text):
    return {
        'object': 'block',
        'type': f'heading_{level}',
        f'heading_{level}': {'rich_text': rich_text(text)}
    }


def make_paragraph(text):
    return {
        'object': 'block',
        'type': 'paragraph',
        'paragraph': {'rich_text': rich_text(text)}
    }


def make_table(cols, rows):
    """cols = int, rows = list of lists of strings"""
    table_rows = []
    for row in rows:
        table_rows.append({
            'object': 'block',
            'type': 'table_row',
            'table_row': {
                'cells': [text_cell(c) for c in row]
            }
        })
    return {
        'object': 'block',
        'type': 'table',
        'table': {
            'table_width': cols,
            'has_column_header': True,
            'has_row_header': False,
            'children': table_rows
        }
    }


def make_divider():
    return {'object': 'block', 'type': 'divider', 'divider': {}}


# First, let's see what's left on the page now
print('=== Current state of Atlas OS ===')
top = get_children(PAGE_ID)
for b in top.get('results', []):
    btype = b.get('type', '')
    data = b.get(btype, {})
    text = ''
    if 'rich_text' in data:
        text = ''.join(t.get('plain_text', '') for t in data.get('rich_text', []))
    elif btype == 'child_database':
        text = b.get('child_database', {}).get('title', '')
    elif btype == 'child_page':
        text = b.get('child_page', {}).get('title', '')
    print(f'  [{btype}] {text[:80]} (id={b["id"]})')

# Now find the key anchor blocks to insert AFTER
# We want to insert tables after their corresponding section headings
# The structure should be:
#   heading_1 Atlas OS
#   paragraph (intro)
#   callout (regla)
#   heading_2 Hoy
#   to_do x3
#   heading_2 Dashboard rapido
#   bullets x4
#   heading_2 Semana
#   numbered x3
#   heading_2 Delegacion por agente
#   bullets x4
#   heading_2 Reglas operativas
#   toggles x2
#   heading_2 Captura rapida
#   paragraph (formato)
#   --- NEW CONTENT BELOW ---
#   heading_3 Prometeo | TradeLab
#   paragraph (desc)
#   table (Prometeo)
#   heading_3 Hestia | Personal / Hogar
#   paragraph (desc)
#   table (Hestia)
#   heading_3 Ares | Entrenamiento
#   paragraph (desc)
#   table (Ares)
#   heading_3 Atlas | Relacion / Fechas clave
#   paragraph (desc)
#   table (Relacion)
#   heading_3 Atlas | Operacion / Sistema
#   paragraph (desc)
#   table (Sistema)
#   divider

# Build the new blocks to append
new_blocks = [
    make_divider(),
    make_heading(3, 'Prometeo | TradeLab / Producto'),
    make_paragraph('Solo tareas tecnicas o de lanzamiento. Notas cortas y accionables.'),
    make_table(7, [
        ['Tarea', 'Estado', 'Tipo', 'Prioridad', 'Impacto', 'Area', 'Notas'],
        ['Validar Paddle webhook', 'En progreso', 'TradeLab', 'Alta', 'Alto', 'Payments', 'Prioridad 1. Revisar handler/ruta, firma/secreto y actualizacion del estado de pago.'],
        ['Validar pagos Paddle', 'Waiting', 'Payment', 'Alta', 'Alto', 'Payments', 'Unificar con webhook o definir si es tarea separada.'],
        ['Comprar dominio', 'Definir', 'Infra', 'Alta', 'Alto', 'Infra', 'Decidir dominio final y ejecutar compra.'],
        ['Ajustar UI dashboard', 'Definir', 'Feature', 'Media', 'Medio', 'Frontend', 'Concretar alcance minimo del ajuste visual.'],
    ]),
    make_heading(3, 'Hestia | Personal / Hogar'),
    make_paragraph('Pendientes domesticos y de vida practica.'),
    make_table(6, [
        ['Tarea', 'Estado', 'Area', 'Prioridad', 'Responsable', 'Notas'],
        ['Comprar mercado', 'Pendiente', 'Hogar', 'Media', 'Hestia', 'Revisar faltantes y cerrar lista.'],
        ['Comprar agua', 'Waiting', 'Hogar', 'Media', 'Hestia', 'Esperando confirmacion de Jorge.'],
        ['Limpiar oficinas', 'Hecho', 'Limpieza', 'Alta', 'Mariela', ''],
        ['Lavar ropa sin mezclar', 'Hecho', 'Ropa', 'Alta', 'Mariela', ''],
    ]),
    make_heading(3, 'Ares | Entrenamiento / Disciplina'),
    make_paragraph('Rutina, recordatorios y bloqueos reales. Fechas claras o no entra.'),
    make_table(5, [
        ['Rutina', 'Tipo', 'Estado', 'Energia', 'Notas'],
        ['Torso A', 'Torso', 'Listo', 'Media', ''],
        ['Pierna A', 'Pierna', 'Listo', 'Alta', ''],
        ['Descanso', 'Descanso', 'Listo', 'Baja', ''],
        ['Pecho 5AM 26/abr/2026', 'Bloqueado', 'Bloqueado', 'Media', 'Fecha inconsistente. Corregir antes de ejecutar.'],
        ['Pedir fotos Smart Project', 'Bloqueado', 'Bloqueado', 'Media', 'Falta definir quien envia y en que canal.'],
    ]),
    make_heading(3, 'Atlas | Relacion / Fechas clave'),
    make_paragraph('Eventos y planes importantes con fecha clara.'),
    make_table(5, [
        ['Item', 'Tipo', 'Fecha', 'Prioridad', 'Estado'],
        ['Cumpleanos novia', 'Fecha especial', '01/09/2026', 'Alta', 'Registrado'],
        ['Cena especial', 'Plan', 'Definir', 'Media', 'Pendiente'],
        ['Comprar flores', 'Regalo', 'Definir', 'Alta', 'Pendiente'],
    ]),
    make_heading(3, 'Atlas | Operacion / Sistema'),
    make_paragraph('Mejoras internas y sistema. Sin siguiente paso, no se queda arriba.'),
    make_table(7, [
        ['Tarea', 'Estado', 'Tipo', 'Prioridad', 'Impacto', 'Area', 'Notas'],
        ['Ideas de viaje siguiente semana', 'Definir', 'Vida practica', 'Alta', 'Medio', 'Viaje', 'Definir rango, presupuesto y compania; proponer 3-5 opciones.'],
        ['Mejorar proactividad OpenClaw', 'Definir', 'Sistema', 'Alta', 'Alto', 'Sistema', 'Convertir en plan operativo corto.'],
    ]),
    make_divider(),
]

print(f'\n=== Appending {len(new_blocks)} new blocks ===')
# Notion API limit: max 100 children per request, we're well under
safe('append all', lambda: append_children(PAGE_ID, new_blocks))

print('\nRebuild complete.')
