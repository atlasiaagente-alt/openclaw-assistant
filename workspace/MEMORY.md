# MEMORY.md

## Operación / OpenClaw

- Para crear nuevos agentes aislados en OpenClaw, existe un playbook replicable en `workspace/agents-setup-playbook.md`.
- Próximo agente objetivo: **Ares** (`⚔️`), enfocado en entrenamiento, consistencia física, hábitos y disciplina.
- Rol de Ares: ayudar a decidir el entrenamiento del día según energía y carga semanal; coordinar el grupo `Smart Project`.
- Personalidad deseada de Ares: directo, motivador, claro y práctico; sin motivación falsa ni teoría en exceso.
- Rutina base de Ares: torso-pierna frecuencia 2 — miércoles, jueves, sábado y domingo.
- Restricción crítica de Ares: solo escribir en `Smart Project` cuando Gustavo hable, hasta nueva orden de Gustavo.
- Caso base ya implementado: **Hestia**.
- Recordar: crear un agente no lo deja automáticamente como sesión persistente conversable; la verificación base se hace con `cmd /c openclaw agent --agent <id> --message "..."`.
- Recordar: para agentes separados, la conversación persistente real llega al conectarlos por canal/binding (por ejemplo peer de WhatsApp), no vía `sessions_spawn`.
- Preferencia actual de Gustavo: usar **un mismo número de WhatsApp** con **múltiples agentes aislados** por dentro, enrutados por contacto/grupo hacia el `agentId` correcto.
- Caso inicial deseado: Jorge (`+573144752380`) debe caer en `hestia`.
- Preferencia operativa: cuando Hestia vaya a hablar con Jorge, debe enviarle los mensajes por WhatsApp.
- Existe un playbook para subir el criterio conversacional de futuros agentes sin cambiar de modelo: `workspace/agents-soul-playbook.md`.
- Patrón recordatorio:
  1. `cmd /c openclaw agents add <id>`
  2. copiar auth desde `main`
  3. no configurar canales en el wizard si la ruta aún no está clara
  4. personalizar `workspace-<id>/IDENTITY.md`, `USER.md` y `SOUL.md`
  5. probar con `cmd /c openclaw agent --agent <id> --message "..."`
  6. luego añadir bindings/routing si hace falta conectarlo a canales
