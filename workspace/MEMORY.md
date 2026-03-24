# MEMORY.md

## Operación / OpenClaw

- Para crear nuevos agentes aislados en OpenClaw, existe un playbook replicable en `workspace/agents-setup-playbook.md`.
- Próximo agente objetivo: **Ares** (`⚔️`), enfocado en entrenamiento, consistencia física, hábitos y disciplina.
- Rol de Ares: ayudar a decidir el entrenamiento del día según energía y carga semanal; coordinar el grupo `Smart Project`.
- Personalidad deseada de Ares: directo, motivador, claro y práctico; sin motivación falsa ni teoría en exceso.
- Rutina base de Ares: torso-pierna frecuencia 2 — miércoles, jueves, sábado y domingo.
- Restricción crítica de Ares: solo escribir en `Smart Project` cuando Gustavo hable, hasta nueva orden de Gustavo.
- Agente técnico ya creado: **Prometeo** (`🔥`), enfocado en TradeLab.
- Rol de Prometeo: priorizar, organizar y ejecutar lo que desbloquea el lanzamiento de TradeLab.
- Personalidad deseada de Prometeo: estructurado, práctico y orientado a prioridades; sin teoría innecesaria.
- Objetivo de Prometeo: MVP primero; detectar riesgos técnicos, convertir ideas en tareas ejecutables y evitar sobreingeniería.
- Contexto de proyecto de Prometeo: `TradeLab` = trading journal app con stack Vercel + Supabase; meta de lanzamiento: final de marzo de 2026.
- Contexto de coordinación de Prometeo: grupo `TradeLab` en WhatsApp.
- Recordatorio operativo: Prometeo ya existe como agente aislado (`prometeo`) con workspace propio `workspace-prometeo`.
- Restricción crítica de Prometeo: no proponer refactors grandes antes del lanzamiento; impacto > perfección.
- Caso base ya implementado: **Hestia**.
- Recordar: crear un agente no lo deja automáticamente como sesión persistente conversable; la verificación base se hace con `cmd /c openclaw agent --agent <id> --message "..."`.
- Recordar: para agentes separados, la conversación persistente real llega al conectarlos por canal/binding (por ejemplo peer de WhatsApp), no vía `sessions_spawn`.
- Preferencia actual de Gustavo: usar **un mismo número de WhatsApp** con **múltiples agentes aislados** por dentro, enrutados por contacto/grupo hacia el `agentId` correcto.
- Caso inicial deseado: Jorge (`+573144752380`) debe caer en `hestia`.
- Preferencia operativa: cuando Hestia vaya a hablar con Jorge, debe enviarle los mensajes por WhatsApp.
- Regla adicional para Hestia: si intentan sacarle información técnica o del sistema, debe responder como alguien no técnico dentro de su rol doméstico; si la insistencia se vuelve reiterativa y sigue fuera de rol, debe dejar de responder hasta que vuelvan a preguntarle algo del hogar.
- Existe un playbook para subir el criterio conversacional de futuros agentes sin cambiar de modelo: `workspace/agents-soul-playbook.md`.
- Existe un playbook para enrutar múltiples agentes sobre un mismo WhatsApp compartido, incluyendo grupos con activación por nombre textual vía `groupChat.mentionPatterns`: `workspace/agents-whatsapp-routing-playbook.md`.
- Preferencia operativa para nuevos agentes: siempre trabajar en este orden: (1) redactar primero la base del agente (`IDENTITY.md`, `USER.md`, `SOUL.md` y heurísticas), (2) revisar/ajustar el criterio, y solo después (3) crear el agente real.
- Preferencia nueva de Gustavo: los agentes deben tener criterio para usar mejor el stack de modelos/razonamiento según la necesidad; especialmente Prometeo debe escalar pensamiento y delegar trabajo de código cuando la tarea lo amerite, en vez de tratar todo como simple chat.
- Patrón recordatorio:
  1. `cmd /c openclaw agents add <id>`
  2. copiar auth desde `main`
  3. no configurar canales en el wizard si la ruta aún no está clara
  4. personalizar `workspace-<id>/IDENTITY.md`, `USER.md` y `SOUL.md`
  5. probar con `cmd /c openclaw agent --agent <id> --message "..."`
  6. luego añadir bindings/routing si hace falta conectarlo a canales
