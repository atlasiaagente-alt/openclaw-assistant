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

def text(content):
    return {'type': 'text', 'text': {'content': content}}

def notion(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method=method)
    for k, v in HEADERS.items():
        req.add_header(k, v)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode('utf-8'))

children = [
    {'object':'block','type':'divider','divider':{}},
    {'object':'block','type':'heading_1','heading_1':{'rich_text':[text('Atlas OS - Home')],'color':'default','is_toggleable':False}},
    {'object':'block','type':'paragraph','paragraph':{'rich_text':[text('Centro de control para decidir rapido, ver prioridades reales y coordinar trabajo entre tu y yo.')],'color':'default'}},
    {'object':'block','type':'callout','callout':{'rich_text':[text('Regla del tablero: arriba vive la decision, abajo viven las tablas fuente.')] ,'color':'blue_background','icon':{'type':'emoji','emoji':'🎯'}}},

    {'object':'block','type':'heading_2','heading_2':{'rich_text':[text('Hoy')],'color':'default','is_toggleable':False}},
    {'object':'block','type':'to_do','to_do':{'rich_text':[text('Resultado clave del dia')],'checked':False,'color':'default'}},
    {'object':'block','type':'to_do','to_do':{'rich_text':[text('Bloqueo principal a resolver')],'checked':False,'color':'default'}},
    {'object':'block','type':'to_do','to_do':{'rich_text':[text('Siguiente paso concreto de menos de 20 minutos')],'checked':False,'color':'default'}},

    {'object':'block','type':'heading_2','heading_2':{'rich_text':[text('Dashboard rapido')],'color':'default','is_toggleable':False}},
    {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Ahora -> lo que esta activo y mueve resultado hoy.')],'color':'default'}},
    {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Siguiente -> lo proximo que entra apenas cierres lo actual.')],'color':'default'}},
    {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Waiting -> cosas que dependen de tercero, respuesta o tiempo.')],'color':'default'}},
    {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Delegado -> trabajo en manos de Atlas, Prometeo, Ares o Hestia.')],'color':'default'}},

    {'object':'block','type':'heading_2','heading_2':{'rich_text':[text('Semana')],'color':'default','is_toggleable':False}},
    {'object':'block','type':'numbered_list_item','numbered_list_item':{'rich_text':[text('Produccion / negocio: lo que empuja ingresos, lanzamiento o entregables.')],'color':'default'}},
    {'object':'block','type':'numbered_list_item','numbered_list_item':{'rich_text':[text('Personal / hogar: mantenimiento de vida, compras, pendientes practicos y eventos.')],'color':'default'}},
    {'object':'block','type':'numbered_list_item','numbered_list_item':{'rich_text':[text('Cuerpo / disciplina: entrenamiento, energia, recuperacion y consistencia.')],'color':'default'}},

    {'object':'block','type':'heading_2','heading_2':{'rich_text':[text('Delegacion por agente')],'color':'default','is_toggleable':False}},
    {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Atlas -> coordinacion general, agenda, correo, seguimiento y criterio operativo.')],'color':'default'}},
    {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Prometeo -> TradeLab, MVP, prioridades tecnicas y desbloqueo de lanzamiento.')],'color':'default'}},
    {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Ares -> entrenamiento del dia, carga semanal, disciplina y consistencia.')],'color':'default'}},
    {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Hestia -> hogar, orden domestico, compras y coordinacion cotidiana.')],'color':'default'}},

    {'object':'block','type':'heading_2','heading_2':{'rich_text':[text('Reglas operativas')],'color':'default','is_toggleable':False}},
    {'object':'block','type':'toggle','toggle':{'rich_text':[text('Estados canonicos')],'color':'default','children':[
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Inbox -> capturado pero aun sin decidir.')],'color':'default'}},
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Definir -> falta claridad o criterio.')],'color':'default'}},
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Listo -> ya se puede ejecutar.')],'color':'default'}},
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('En progreso -> trabajo activo.')],'color':'default'}},
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Waiting / Bloqueado -> no depende de accion inmediata propia.')],'color':'default'}},
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Hecho -> cerrado, fuera del foco.')],'color':'default'}},
    ]}},
    {'object':'block','type':'toggle','toggle':{'rich_text':[text('Prioridad')],'color':'default','children':[
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Alta -> mueve resultado o evita dano.')],'color':'default'}},
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Media -> importante, pero puede esperar un poco.')],'color':'default'}},
        {'object':'block','type':'bulleted_list_item','bulleted_list_item':{'rich_text':[text('Baja -> mantenimiento, idea o mejora no critica.')],'color':'default'}},
    ]}},

    {'object':'block','type':'heading_2','heading_2':{'rich_text':[text('Captura rapida')],'color':'default','is_toggleable':False}},
    {'object':'block','type':'quote','quote':{'rich_text':[text('[Area] | [Resultado esperado] | [Responsable] | [Estado] | [Prioridad] | [Siguiente paso]')],'color':'default'}},
    {'object':'block','type':'paragraph','paragraph':{'rich_text':[text('Ejemplo: TradeLab | cerrar pagos MVP | Prometeo | En progreso | Alta | revisar flujo de checkout')],'color':'gray'}},

    {'object':'block','type':'heading_2','heading_2':{'rich_text':[text('Debajo: referencia y tablas')],'color':'default','is_toggleable':False}},
    {'object':'block','type':'paragraph','paragraph':{'rich_text':[text('Las secciones antiguas y las tablas existentes quedan abajo como fuente de verdad y archivo operativo.')],'color':'default'}},
]

resp = notion('PATCH', f'https://api.notion.com/v1/blocks/{PAGE_ID}/children', {'children': children})
print('OK')
