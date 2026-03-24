# Google Workspace / Gmail notes

## Estado

La integración ya está operativa en esta máquina mediante `gog`.

## Cuenta autenticada detectada

- `atlas.ia.agente@gmail.com`
- perfil: `default`
- auth: `oauth`

## Servicios disponibles

- gmail
- calendar
- drive
- contacts
- docs
- sheets
- tasks
- y otros servicios Google listados por `gog auth list`

## Comprobación rápida

```bat
cmd /c gog auth list
```

## Uso base

- Buscar correos: `gog gmail search 'newer_than:7d' --max 10`
- Buscar mensajes individuales: `gog gmail messages search "in:inbox" --max 20`
- Ver eventos: `gog calendar events primary --from <iso> --to <iso>`

## Nota operativa

Confirmar antes de enviar correos o crear eventos. Para lectura, búsqueda y revisión de inbox/calendario, esta integración ya se puede usar directamente.
