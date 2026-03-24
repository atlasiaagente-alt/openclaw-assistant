# Notion integration notes

## Estado

Sí hay integración usable con Notion en esta máquina.

## Método

Usar la API oficial de Notion con token disponible en variable de entorno local:

- `NOTION_TOKEN`

Cabeceras base:

```powershell
$headers = @{
  'Authorization' = "Bearer $env:NOTION_TOKEN"
  'Notion-Version' = '2025-09-03'
  'Content-Type' = 'application/json'
}
```

## Operaciones base

### Buscar páginas

```powershell
Invoke-RestMethod -Method Post -Uri 'https://api.notion.com/v1/search' -Headers $headers -Body '{"query":"Atlas OS"}'
```

### Leer bloques hijos

```powershell
Invoke-RestMethod -Method Get -Uri 'https://api.notion.com/v1/blocks/<block_or_page_id>/children?page_size=100' -Headers $headers
```

### Añadir bloques

```powershell
Invoke-RestMethod -Method Patch -Uri 'https://api.notion.com/v1/blocks/<block_or_page_id>/children' -Headers $headers -Body $bodyJson
```

### Archivar bloque

```powershell
Invoke-RestMethod -Method Patch -Uri 'https://api.notion.com/v1/blocks/<block_id>' -Headers $headers -Body '{"archived":true}'
```

## Página principal

- Nombre: `Atlas OS`
- Uso: tablero operativo visual / seguimiento de tareas

## Nota operativa

La API puede dar problemas de encoding con emojis/símbolos en algunos flujos de PowerShell. Preferir texto limpio/ASCII cuando algo visual se rompa.
