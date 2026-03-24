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

resp = notion('GET', f'https://api.notion.com/v1/blocks/{PAGE_ID}/children?page_size=100')
results = resp['results']

archive_ids = []
for block in results:
    bid = block['id']
    typ = block['type']
    text = ''
    if typ in ('heading_1','heading_2','heading_3','paragraph','quote','bulleted_list_item','numbered_list_item','to_do','toggle','callout'):
        payload = block[typ]
        rt = payload.get('rich_text', [])
        text = ''.join(part.get('plain_text','') for part in rt)

    if text in {
        'Work Board',
        'Vista rapida para ver que se esta moviendo, quien lo lleva y donde esta atascado.',
        'Estados: Inbox | Definir | Listo | En progreso | En espera | Bloqueado | Hecho',
        'Agentes: Atlas | Hestia | Prometeo | Ares',
        'Prioridad: Alta | Media | Baja',
        'Atlas OS',
        'Tablero de trabajo para ver rapidamente que se esta haciendo, que esta bloqueado y que sigue.',
        'Areas activas',
        'TradeLab: pagos, dominio, dashboard',
        'Hogar: limpieza, mercado, desayuno, ropa',
        'Training: torso, pierna, descanso',
        'Life: cumpleanos, cena, flores',
        'Tablas base',
        'Debajo de esta cabecera quedan tus tablas actuales. Desde ahi puedes meter pendientes y yo los ire reflejando en el tablero visual.',
        'Dashboard operativo',
        'Vista pensada para decidir rapido: que importa hoy, que esta en movimiento, donde hay bloqueo y que sigue.',
        'Uso simple: captura en tablas base, mira el foco, ejecuta y revisa bloqueos.',
        'Foco de hoy',
        '1 resultado clave del dia',
        '1 bloqueo a resolver hoy',
        '1 siguiente paso concreto',
        'Panel de decision',
        'Ahora: lo que esta activo y merece atencion inmediata.',
        'Siguiente: cola corta de lo proximo en entrar.',
        'Bloqueos: cosas detenidas por dependencia, decision o energia.',
        'Delegado: que esta en manos de Atlas, Hestia, Prometeo o Ares.',
        'Ritmo semanal',
        'Lunes a miercoles: empuje de produccion y negocio.',
        'Jueves a domingo: entrenamiento, vida personal y mantenimiento.',
        'Revisiones: 8:00 AM y 7:00 PM para correo, calendario y prioridades.',
        'Agentes y duenos',
        'Atlas -> router, agenda, email y coordinacion general.',
        'Prometeo -> TradeLab, MVP y desbloqueo tecnico.',
        'Ares -> entrenamiento, disciplina y carga semanal.',
        'Hestia -> hogar y coordinacion domestica.',
        'Reglas del tablero',
        'Plantilla rapida de captura',
        '[Area] | [Resultado esperado] | [Responsable] | [Estado] | [Prioridad] | [Siguiente paso]',
        'Debajo: referencia y tablas',
        'Las secciones antiguas y las tablas existentes quedan abajo como fuente de verdad y archivo operativo.',
    }:
        archive_ids.append(bid)
    elif typ == 'paragraph' and not text.strip():
        archive_ids.append(bid)

for bid in archive_ids:
    notion('PATCH', f'https://api.notion.com/v1/blocks/{bid}', {'archived': True})

print(f'archived={len(archive_ids)}')
