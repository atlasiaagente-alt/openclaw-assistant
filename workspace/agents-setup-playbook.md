# Playbook: crear un agente nuevo en OpenClaw

## Caso base: Hestia

Este documento resume cómo se creó **Hestia** para poder replicarlo con futuros agentes.

## 1) Crear el agente

Comando usado:

```bat
cmd /c openclaw agents add hestia
```

Durante el wizard se eligió:

- Workspace: `C:\Users\Gustavo\.openclaw\workspace-hestia`
- Copy auth profiles from "main": **Yes**
- Configure model/auth now: **No**
- Configure chat channels now: **No**

## 2) Resultado técnico

OpenClaw añadió en `C:\Users\Gustavo\.openclaw\openclaw.json`:

- `agents.list[].id = "hestia"`
- `workspace = "C:\\Users\\Gustavo\\.openclaw\\workspace-hestia"`
- `agentDir = "C:\\Users\\Gustavo\\.openclaw\\agents\\hestia\\agent"`

Y creó:

- Workspace: `C:\Users\Gustavo\.openclaw\workspace-hestia`
- Sessions: `C:\Users\Gustavo\.openclaw\agents\hestia\sessions`
- Agent state/auth: `C:\Users\Gustavo\.openclaw\agents\hestia\agent`

## 3) Archivos de identidad/persona

Se personalizaron estos archivos en el workspace del agente:

- `IDENTITY.md`
- `USER.md`
- `SOUL.md`

Patrón replicable:

- `IDENTITY.md` → nombre, emoji, vibe
- `USER.md` → quién es Gustavo para ese agente y contactos relevantes
- `SOUL.md` → rol, tono, límites, reglas de escalamiento

## 4) Qué NO quedó hecho todavía

- No se configuró binding de canal hacia Hestia.
- No se conectó WhatsApp por contacto todavía.
- No se creó routing automático por peer.

## 5) Cómo probar un agente nuevo

Ejemplo por CLI:

```bat
cmd /c openclaw agent --agent hestia --message "Preséntate en una línea"
```

Esto sirve como prueba mínima de que:

- el agente existe
- su workspace carga bien
- su identidad/persona responde

## 6) Sobre sesiones persistentes

Tener un agente creado **no** implica que ya exista una sesión viva con label reutilizable.

Diferencia práctica:

- `openclaw agent --agent <id> --message "..."` → invoca al agente por CLI y devuelve respuesta
- sesión persistente conversable → normalmente aparece cuando el agente queda conectado a un canal o routing real (binding)

Conclusión práctica para replicar:

- para agentes separados de OpenClaw, la verificación base y segura es la invocación por CLI
- si se quiere conversación persistente real, el siguiente paso no es `sessions_spawn`, sino **binding/routing de canal hacia ese agentId**
- en WhatsApp con un solo número, eso se resuelve con bindings por peer/contacto hacia agentes distintos

Por ahora, la forma segura y replicable para verificar un agente nuevo es la invocación por CLI.
La sesión persistente debe añadirse después mediante canal + binding.

## 7) Patrón para futuros agentes

Repetir:

1. `cmd /c openclaw agents add <id>`
2. copiar auth desde `main`
3. no configurar canales en el wizard si todavía no está clara la ruta
4. editar `workspace-<id>\IDENTITY.md`
5. editar `workspace-<id>\USER.md`
6. editar `workspace-<id>\SOUL.md`
7. probar con `openclaw agent --agent <id> --message "..."`
8. luego añadir bindings/routing

## 7) Notas

- En PowerShell directo, `openclaw` puede chocar con execution policy. Usar:

```bat
cmd /c openclaw ...
```

- Para aislar personalidades de verdad, cada agente debe tener su propio workspace y agentDir.
