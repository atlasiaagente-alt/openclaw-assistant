# MEMORY.md

## Operación / OpenClaw

- Para crear nuevos agentes aislados en OpenClaw, existe un playbook replicable en `workspace/agents-setup-playbook.md`.
- Política global deseada por Gustavo: `Atlas` es el router de modelos; preferir Ollama para trabajo barato/seguro, Claude Code como builder por defecto para código, ChatGPT como thinker por defecto para razonamiento, y Opus/GPT-5 solo para casos complejos o de alto riesgo. Documento base: `workspace/model-routing-policy.md`.
- Próximo agente objetivo: **Ares** (`⚔️`), enfocado en entrenamiento, consistencia física, hábitos y disciplina.
- Rol de Ares: ayudar a decidir el entrenamiento del día según energía y carga semanal; coordinar el grupo `Smart Project`.
- Personalidad deseada de Ares: directo, motivador, claro y práctico; sin motivación falsa ni teoría en exceso.
- Rutina base de Ares: torso-pierna frecuencia 2 — miércoles, jueves, sábado y domingo.
- Restricción crítica actualizada de Ares en `Smart Project`: puede escribir cuando Gustavo hable o cuando Atlas lo active/coordine explícitamente para ejecutar una tarea; fuera de eso, no debe intervenir por cuenta propia.
- Preferencia operativa para grupos de WhatsApp compartidos: evitar que Atlas y el agente dueño del grupo (por ejemplo Ares en `Smart Project`) escriban o coordinen sobre el mismo chat al mismo tiempo; si Atlas necesita empujar algo, primero debe dejar liberar el canal y luego disparar solo al agente responsable para evitar colisiones de entrega/enrutado.
- Nueva regla operativa crítica: en coordinación entre agentes, `coordinado` no significa `ejecutado` y `ejecutado` no significa `entregado`. Atlas no debe reportar tareas como hechas sin confirmación suficiente del agente responsable y, cuando aplique, evidencia real de entrega en el canal externo.
- Agente técnico ya creado: **Prometeo** (`🔥`), enfocado en TradeLab.
- Rol de Prometeo: priorizar, organizar y ejecutar lo que desbloquea el lanzamiento de TradeLab.
- Repositorio local principal de TradeLab para Prometeo: `C:\Users\Gustavo\Documents\tradelab-front`.
- Flujo de trabajo de Prometeo: trabajar sobre la rama `agent-workspace` y abrir pull requests hacia `main`.
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
- Existe un mini playbook para saber dónde documentar cada capa de la comunicación entre agentes (comportamiento, relación, routing, memoria estratégica y tooling): `workspace/agent-communication-organization-playbook.md`.
- Existe un playbook específico para handoff y confirmación entre agentes, para evitar falsos positivos de ejecución/entrega: `workspace/agent-handoff-confirmation-playbook.md`.
- Preferencia operativa para nuevos agentes: siempre trabajar en este orden: (1) redactar primero la base del agente (`IDENTITY.md`, `USER.md`, `SOUL.md` y heurísticas), (2) revisar/ajustar el criterio, y solo después (3) crear el agente real.
- Preferencia nueva de Gustavo: los agentes deben tener criterio para usar mejor el stack de modelos/razonamiento según la necesidad; especialmente Prometeo debe escalar pensamiento y delegar trabajo de código cuando la tarea lo amerite, en vez de tratar todo como simple chat.
- Política global deseada por Gustavo: `Atlas` es el router de modelos; preferir Ollama para trabajo barato/seguro, Claude Code como builder por defecto para código, ChatGPT como thinker por defecto para razonamiento, y Opus/GPT-5 solo para casos complejos o de alto riesgo. Documento base: `workspace/model-routing-policy.md`.
- Tener presente para todos los agentes la guía de seguridad de OpenClaw (`/gateway/security`): operar bajo modelo de asistente personal con un solo límite de confianza, mínimo privilegio, DMs aislados por contacto, canales/restricciones cuidadas y no asumir aislamiento multi-tenant fuerte. Notas internas: `workspace/security-baseline-notes.md`.
- Recordar: sí existe integración usable con Notion en esta máquina vía API token local (`NOTION_TOKEN`), y Gustavo quiere usarla como tablero operativo vivo.
- Página operativa principal ya identificada: `Atlas OS` en Notion.
- Lección operativa importante: si `exec` falla con `allowlist miss`, revisar `openclaw approvals get`; en esta máquina la solución mínima útil para destrabar trabajo local del agente `main` fue añadir a la allowlist `C:\Users\Gustavo\AppData\Roaming\npm\openclaw.cmd`, `C:\Windows\System32\cmd.exe` y `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`.
- Rutina deseada: revisar Notion / `Atlas OS` todos los días a las 8:00 AM y, con base en eso, coordinar trabajo con los subagentes.
- Rutina ya configurada: revisión automática de `Atlas OS` 3 veces al día (8:00 AM, 12:00 PM, 7:00 PM, America/Bogota) vía cron, con análisis de estados, detección de cambios y coordinación/orden a subagentes según pendientes.
- Estructura actual deseada de `Atlas OS`: dashboard operativo con Home, Hoy, Dashboard rápido, Semana, Delegación por agente, Reglas operativas y Captura rápida; tablas homogéneas con títulos por responsable y estados canónicos visuales (`📥 Inbox`, `🟣 Definir`, `🟡 Listo`, `🔵 En progreso`, `🕒 Waiting`, `⛔ Bloqueado`, `✅ Hecho`).
- Regla operativa actual para `Atlas OS`: Atlas direcciona el trabajo según el agente responsable; en cada revisión debe coordinar y empujar al subagente dueño de los pendientes para su ejecución.
- Regla crítica adicional para futuras ejecuciones: la primera tabla visible de `Atlas OS` debe tratarse como inbox operativo principal. Si una fila allí ya tiene área/responsable claro (por ejemplo `Ares` para entrenamiento), Atlas no debe limitarse a leerla o resumirla; debe delegarla activamente al agente dueño y luego hacer seguimiento.
- Regla de escalamiento: si un subagente responde pero no toma una decisión clara, no ejecuta, o queda ambiguo, Atlas debe destrabarlo o escalar el problema explícitamente a Gustavo; no debe dejar el caso en silencio ni reportarlo implícitamente como resuelto.
- Regla dinámica adicional: cuando una tarea o subagente quede bloqueado por ambigüedad pequeña (por ejemplo fecha pasada, estado incierto o falta de confirmación menor), Atlas debe intentar destrabar con una acción segura y natural en vez de frenarse: hacer una pregunta breve en el canal correcto si aplica, reencaminar al agente a la siguiente acción útil o pasar a otra actividad mientras espera respuesta. Objetivo: dinamizar, no congelarse.
- Regla operativa nueva para Atlas con subagentes: no devolverles accionables pequeños. Si la acción es avisar, preguntar corto, confirmar algo simple o tomar una decisión menor dentro de su rol, Atlas debe empujarlos a ejecutarla directamente.
- Orden de acción operativo a respetar al coordinarlos: Ares prioriza `Smart Project` -> Atlas -> Gustavo; Hestia prioriza Gustavo y Jorge en paralelo cuando aplique, luego Mariela; Prometeo prioriza canal/grupo de `TradeLab` -> Atlas.
- Principio operativo central de Atlas para futuras sesiones: actuar como orquestador del trabajo, usando `Atlas OS` para decidir qué corresponde a cada agente y mover la ejecución hacia el responsable correcto.
- Correo/Google Workspace ya operativo en esta máquina vía `gog`; cuenta autenticada detectada: `atlas.ia.agente@gmail.com` con acceso a Gmail/Calendar/Drive/Contacts/Docs/Sheets/Tasks. Usarlo en futuras sesiones cuando haga falta.
- Rutina deseada con correo: revisar diariamente `atlas.ia.agente@gmail.com`, detectar reenvíos/pendientes/plazos útiles y recordarle a Gustavo por WhatsApp (`+573183718246`) lo que tenga pendiente para ese día y próximos deadlines.
- Además, cuando aplique, citar/agendar esos pendientes relevantes hacia el correo/calendario de Gustavo: `toledo970501@gmail.com`.
- Paneo deseado dos veces al día: 8:00 AM y 7:00 PM, incluyendo WhatsApp a Gustavo y organización de lo relevante en calendario hacia `toledo970501@gmail.com`.
- Ejemplo vigente a recordar: desde hoy Gustavo tiene 3 días para realizar un challenge de ZooLATECH.
- Patrón recordatorio:
  1. `cmd /c openclaw agents add <id>`
  2. copiar auth desde `main`
  3. no configurar canales en el wizard si la ruta aún no está clara
  4. personalizar `workspace-<id>/IDENTITY.md`, `USER.md` y `SOUL.md`
  5. probar con `cmd /c openclaw agent --agent <id> --message "..."`
  6. luego añadir bindings/routing si hace falta conectarlo a canales
