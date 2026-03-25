# Playbook - Dónde vive cada cosa de la comunicación entre agentes

Objetivo: evitar que las reglas de comunicación, routing y comportamiento de agentes queden dispersas entre memoria, prompts y notas operativas.

## Regla madre

Separar siempre estas capas:

1. **Identidad y criterio conversacional**
2. **Relación con la persona o contexto**
3. **Routing y activación por canal/chat/grupo**
4. **Coordinación global entre agentes**
5. **Detalles operativos de herramientas/canales**

---

## 1) `SOUL.md` → Cómo habla y decide el agente

Aquí va:

- personalidad
- tono
- criterio conversacional
- límites de comportamiento
- cuándo hablar y cuándo callar
- cómo responder fuera de rol
- estilo de intervención en grupos

Ejemplos:

- “Ares debe ser directo, motivador y práctico.”
- “Hestia debe responder como alguien no técnico dentro de su rol doméstico.”
- “No dar teoría innecesaria.”

**No poner aquí:**

- números de teléfono
- group ids
- bindings
- comandos técnicos

---

## 2) `USER.md` → Quién es la otra parte

Aquí va:

- quién es la persona
- cómo llamarla
- relación con el agente
- idioma
- contexto humano relevante
- preferencias de trato

Ejemplos:

- Jorge es contacto directo de Hestia
- Gustavo es el dueño y orquestador humano
- idioma principal y estilo preferido

**No poner aquí:**

- routing técnico
- comandos
- config de canal

---

## 3) Playbooks técnicos / config → Cómo llega el mensaje al agente

Aquí va todo lo de routing real:

- bindings por contacto o grupo
- `peer.kind`
- `peer.id`
- `group-jid`
- `groupChat.mentionPatterns`
- reglas de activación por nombre
- reinicios/recargas necesarias
- diagnóstico de logs

Documento actual principal:

- `workspace/agents-whatsapp-routing-playbook.md`

Este es el lugar correcto para responder preguntas como:

- “¿Cómo cae Jorge en Hestia?”
- “¿Cómo hago que Ares responda en Smart Project?”
- “¿Qué hago si el binding existe pero el agente no despierta?”

---

## 4) `MEMORY.md` → Decisiones estratégicas duraderas

Aquí va:

- qué arquitectura se decidió usar
- qué agente es dueño de qué chat o dominio
- restricciones críticas duraderas
- reglas de coordinación entre agentes
- preferencias del humano que deban persistir entre sesiones

Ejemplos:

- usar un mismo número de WhatsApp con múltiples agentes aislados
- Atlas actúa como orquestador
- evitar colisiones de escritura entre Atlas y el agente dueño del grupo
- Ares solo escribe en `Smart Project` cuando Gustavo hable, hasta nueva orden

**No poner aquí salvo excepción:**

- comandos concretos
- checks técnicos rutinarios
- detalles de tooling que pertenecen a `TOOLS.md`

---

## 5) `TOOLS.md` → Chuleta operativa local

Aquí va:

- variables de entorno útiles
- comandos frecuentes
- checks rápidos
- herramientas instaladas
- rutas locales
- detalles prácticos para operar

Ejemplos:

- cómo llamar la API de Notion con `NOTION_TOKEN`
- comando de transcripción con `whisper-bridge.py`
- binarios disponibles como `ffmpeg`

**No poner aquí:**

- decisiones estratégicas del sistema
- personalidad del agente
- reglas de ownership de chats a largo plazo

---

## Regla práctica rápida

Si la pregunta es...

- **“¿Cómo debe comportarse el agente?”** → `SOUL.md`
- **“¿Quién es esta persona para el agente?”** → `USER.md`
- **“¿Cómo se enruta o activa en el canal?”** → playbook técnico / config
- **“¿Qué decidimos a nivel sistema y coordinación?”** → `MEMORY.md`
- **“¿Qué comando o herramienta uso aquí?”** → `TOOLS.md`

---

## Caso WhatsApp compartido

Para agentes múltiples sobre un mismo número:

- arquitectura general y ownership → `MEMORY.md`
- comportamiento del agente en chat/grupo → `SOUL.md`
- relación con la persona/contacto → `USER.md`
- bindings, `group-jid`, mention patterns → `agents-whatsapp-routing-playbook.md`
- comandos/checks locales → `TOOLS.md`

---

## Regla de mantenimiento

Cuando algo nuevo aparezca, decidir primero si es:

- una **decisión duradera**
- una **regla de comportamiento**
- una **relación humana**
- una **implementación técnica**
- o una **nota operativa local**

Y guardarlo en el archivo correcto en vez de duplicarlo por todos lados.
