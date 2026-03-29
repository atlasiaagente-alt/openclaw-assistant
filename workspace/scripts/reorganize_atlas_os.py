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
        print('error', label, e.code, body)
    except Exception as e:
        print('error', label, repr(e))


def rich_text(content):
    return [{"type": "text", "text": {"content": content}}]


def patch_block(block_id, block_type, content):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {
        block_type: {"rich_text": rich_text(content)}
    })


def patch_heading(block_id, level, content):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {
        f'heading_{level}': {"rich_text": rich_text(content)}
    })


def patch_todo(block_id, content, checked=False):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {
        'to_do': {"rich_text": rich_text(content), 'checked': checked}
    })


def patch_bullet(block_id, content):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {
        'bulleted_list_item': {"rich_text": rich_text(content)}
    })


def patch_numbered(block_id, content):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {
        'numbered_list_item': {"rich_text": rich_text(content)}
    })


def patch_callout(block_id, content, emoji='⚡'):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {
        'callout': {
            'rich_text': rich_text(content),
            'icon': {'type': 'emoji', 'emoji': emoji}
        }
    })


def patch_toggle(block_id, content):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {
        'toggle': {"rich_text": rich_text(content)}
    })


def text_cell(content):
    return [{"type": "text", "text": {"content": content}}]


def replace_row(row_id, cells):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{row_id}', {
        'table_row': {'cells': [text_cell(c) for c in cells]}
    })

ops = [
    ('title', lambda: patch_heading('32d0a0b1-97cc-81eb-b5b5-d0ab45093054', 1, 'Atlas OS')),
    ('intro', lambda: patch_block('32d0a0b1-97cc-816c-94c3-d7f4b95fcb86', 'paragraph', 'Sistema operativo personal. Arriba solo va lo que ayuda a decidir rapido; abajo queda el detalle por area.')),
    ('callout', lambda: patch_callout('32d0a0b1-97cc-8166-a617-d5d6176b18a7', 'Regla del tablero: arriba vive la decision; abajo viven las listas fuente. Sin basura visual, sin duplicados y sin notas eternas.', '⚡')),
    ('hoy', lambda: patch_heading('32d0a0b1-97cc-8186-9dd8-c0f1c1630cea', 2, 'Hoy')),
    ('todo1', lambda: patch_todo('32d0a0b1-97cc-812a-9665-cb98b0a619be', 'Resultado clave del dia', False)),
    ('todo2', lambda: patch_todo('32d0a0b1-97cc-818f-a166-d323839bc998', 'Bloqueo principal a resolver', False)),
    ('todo3', lambda: patch_todo('32d0a0b1-97cc-8141-9472-e8e361652011', 'Siguiente paso concreto (<20 min)', False)),
    ('dashboard', lambda: patch_heading('32d0a0b1-97cc-810f-817a-e214ab647b7b', 2, 'Dashboard rapido')),
    ('b1', lambda: patch_bullet('32d0a0b1-97cc-813b-bc1e-d68455dc711e', 'Ahora -> tareas activas que mueven resultado hoy.')),
    ('b2', lambda: patch_bullet('32d0a0b1-97cc-81d3-9113-e9e8bbf4de85', 'Siguiente -> lo proximo que entra apenas cierres lo actual.')),
    ('b3', lambda: patch_bullet('32d0a0b1-97cc-810d-acea-f584c3b26cdc', 'Waiting -> depende de tercero, respuesta o fecha.')),
    ('b4', lambda: patch_bullet('32d0a0b1-97cc-81da-9617-e1b0a95470f4', 'Delegado -> trabajo en manos de Atlas, Prometeo, Hestia o Ares.')),
    ('semana', lambda: patch_heading('32d0a0b1-97cc-81c8-b718-cde64bd8b0c0', 2, 'Semana')),
    ('n1', lambda: patch_numbered('32d0a0b1-97cc-8117-b585-ceab23ac2d71', 'Negocio / producto -> lo que empuja ingresos, lanzamiento o entregables.')),
    ('n2', lambda: patch_numbered('32d0a0b1-97cc-81b6-92a4-d8380359bf47', 'Personal / hogar -> mantenimiento de vida, compras y pendientes practicos.')),
    ('n3', lambda: patch_numbered('32d0a0b1-97cc-8167-8420-e2b4e3b27c96', 'Cuerpo / disciplina -> entrenamiento, energia, recuperacion y consistencia.')),
    ('delegacion', lambda: patch_heading('32d0a0b1-97cc-8154-9b98-d4b136daa457', 2, 'Delegacion por agente')),
    ('d1', lambda: patch_bullet('32d0a0b1-97cc-812f-b6bb-db5eae489287', 'Atlas -> coordinacion general, agenda, correo, seguimiento y criterio operativo.')),
    ('d2', lambda: patch_bullet('32d0a0b1-97cc-811a-be87-f0b9a5ecaa1b', 'Prometeo -> TradeLab, MVP, prioridades tecnicas y desbloqueo de lanzamiento.')),
    ('d3', lambda: patch_bullet('32d0a0b1-97cc-8104-82c7-c587db51f6c3', 'Ares -> entrenamiento del dia, carga semanal, disciplina y consistencia.')),
    ('d4', lambda: patch_bullet('32d0a0b1-97cc-81c7-bfe0-f0517672e933', 'Hestia -> hogar, orden domestico, compras y coordinacion cotidiana.')),
    ('reglas', lambda: patch_heading('32d0a0b1-97cc-81bf-848d-ed8f11cd6345', 2, 'Reglas operativas')),
    ('t1', lambda: patch_toggle('32d0a0b1-97cc-8180-8daa-ec0a8f205718', 'Estados canonicos')),
    ('t2', lambda: patch_toggle('32d0a0b1-97cc-8135-b8f1-c33b26c4b18a', 'Prioridad')),
    ('captura', lambda: patch_heading('32d0a0b1-97cc-81e9-be47-e765ca3e4e96', 2, 'Captura rapida')),
    ('captura_fmt', lambda: patch_block('32d0a0b1-97cc-8129-be42-d3cfad5ba115', 'paragraph', 'Formato: Area | tarea | responsable | estado | prioridad | siguiente paso')),
    ('prom_title', lambda: patch_block('32d0a0b1-97cc-801b-9f2a-d8a948d75571', 'paragraph', 'Prometeo | TradeLab / Producto')),
    ('prom_desc', lambda: patch_block('32d0a0b1-97cc-817c-895b-e0350ce04d55', 'paragraph', 'Solo tareas tecnicas o de lanzamiento. Notas cortas y accionables.')),
    ('hes_title', lambda: patch_block('32d0a0b1-97cc-8198-9166-e10da6999e69', 'paragraph', 'Hestia | Personal / Hogar')),
    ('hes_desc', lambda: patch_block('32d0a0b1-97cc-817d-95a7-c64a6f48e589', 'paragraph', 'Pendientes domesticos y de vida practica. Sin historiales largos dentro de cada fila.')),
    ('ares_title', lambda: patch_block('32d0a0b1-97cc-8162-8040-dfb1058545a3', 'paragraph', 'Ares | Entrenamiento / Disciplina')),
    ('ares_desc', lambda: patch_block('32d0a0b1-97cc-8199-ba9d-f1f598dfeb28', 'paragraph', 'Rutina, recordatorios y bloqueos reales. Fechas claras o no entra.')),
    ('rel_title', lambda: patch_block('32d0a0b1-97cc-8149-b08a-fa2133a57fcb', 'paragraph', 'Atlas | Relacion / Fechas clave')),
    ('rel_desc', lambda: patch_block('32d0a0b1-97cc-8188-9270-e48299f19b90', 'paragraph', 'Eventos y planes importantes con fecha clara y accion concreta.')),
    ('sys_title', lambda: patch_block('32d0a0b1-97cc-815f-b40c-cf5b3509ec5d', 'paragraph', 'Atlas | Operacion / Sistema')),
    ('sys_desc', lambda: patch_block('32d0a0b1-97cc-81e0-b501-fabfb357994f', 'paragraph', 'Mejoras internas, sistema y operacion de Atlas. Si no tiene siguiente paso, no se queda arriba.')),
    ('row1', lambda: replace_row('32e0a0b1-97cc-814f-9ddb-f6d7f844458b', ['Validar Paddle webhook','En progreso','TradeLab','Alta','Alto','Payments','Owner: Prometeo. Prioridad actual. Revisar ruta/handler, firma/secreto y actualizacion del estado de pago.'])),
    ('row2', lambda: replace_row('32e0a0b1-97cc-8181-b520-f71ee300d7e3', ['Comprar dominio','Definir','Infra','Alta','Alto','Infra','Decidir dominio final y primer paso de compra. No mezclar con otras tareas.'])),
    ('row3', lambda: replace_row('32e0a0b1-97cc-8128-b7d5-cf8c6f957919', ['Ajustar UI dashboard','Definir','Feature','Media','Medio','Frontend','Pendiente de concretar alcance minimo del ajuste visual.'])),
    ('row4', lambda: replace_row('32e0a0b1-97cc-81bc-a0ae-e8d23fc2da0c', ['Comprar mercado','Pendiente hoy','Hogar','Media','','','Owner: Hestia. Revisar faltantes y cerrar lista de compra de hoy.'])),
    ('row5', lambda: replace_row('32e0a0b1-97cc-8126-baae-cb00c02f06fa', ['Comprar agua segun tablero','Waiting','Hogar','Media','','','Esperando confirmacion de Jorge sobre si ya hace falta pedir el agua.'])),
    ('row6', lambda: replace_row('32e0a0b1-97cc-8184-b75c-fda2f5ee1925', ['Entrenamiento de pecho manana 5AM 26/abril/2026','Bloqueado','Entrenamiento','Media','','','Fecha inconsistente. Corregir fecha/rutina real antes de ejecutar cualquier aviso.'])),
    ('row7', lambda: replace_row('32e0a0b1-97cc-815e-a3b2-e56cb41f4978', ['Pedir fotos para el grupo de smart project','Bloqueado','Entrenamiento','Media','','','Falta definir quien debe enviar las fotos y en que canal exacto debe salir la solicitud.'])),
    ('row8', lambda: replace_row('32e0a0b1-97cc-8128-9bd9-ec5e03f0e840', ['Pierna 5AM manana 24/marzo/2026','Recordatorio','Listo','Alta','','','Recordatorio viejo o historico; revisar si debe archivarse para no contaminar la vista.'])),
    ('row9', lambda: replace_row('32e0a0b1-97cc-81b8-beba-dc1f3958b3fb', ['Cena especial','Plan','Definir','Media','Listo'])),
    ('row10', lambda: replace_row('32e0a0b1-97cc-81fe-bc25-e66f7fdca10e', ['Comprar flores','Regalo','Definir','Alta','Listo'])),
    ('row11', lambda: replace_row('32e0a0b1-97cc-81ad-bd93-c2116f8e6571', ['Ideas de viaje para la siguiente semana','Definir','Vida practica','Alta','Medio','Viaje','Definir rango, presupuesto y compania; luego proponer 3-5 opciones concretas.'])),
    ('row12', lambda: replace_row('32e0a0b1-97cc-8124-aa93-dac5976fb1f1', ['Mejorar proactividad de OpenClaw','Definir','Sistema','Alta','Alto','Sistema','Convertir en plan operativo corto: triggers, rutina y seguimiento.'])),
]

for label, fn in ops:
    safe(label, fn)

print('Atlas OS reorganizado (best effort).')
