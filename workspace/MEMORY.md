# MEMORY.md

## Operación / OpenClaw

- Para crear nuevos agentes aislados en OpenClaw, existe un playbook replicable en `workspace/agents-setup-playbook.md`.
- Caso base ya implementado: **Hestia**.
- Recordar: crear un agente no lo deja automáticamente como sesión persistente conversable; la verificación base se hace con `cmd /c openclaw agent --agent <id> --message "..."`.
- Patrón recordatorio:
  1. `cmd /c openclaw agents add <id>`
  2. copiar auth desde `main`
  3. no configurar canales en el wizard si la ruta aún no está clara
  4. personalizar `workspace-<id>/IDENTITY.md`, `USER.md` y `SOUL.md`
  5. probar con `cmd /c openclaw agent --agent <id> --message "..."`
  6. luego añadir bindings/routing si hace falta conectarlo a canales
