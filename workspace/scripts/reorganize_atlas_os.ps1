$ErrorActionPreference = 'Stop'

$headers = @{
  'Authorization' = "Bearer $env:NOTION_TOKEN"
  'Notion-Version' = '2022-06-28'
  'Content-Type' = 'application/json'
}

$pageId = '3290a0b1-97cc-801a-8240-e78d3bfe0e74'

function T([string]$content) {
  return @{
    type = 'text'
    text = @{ content = $content }
  }
}

function Append-Children($parentId, $children) {
  $body = @{ children = $children } | ConvertTo-Json -Depth 100 -Compress
  try {
    Invoke-RestMethod -Method Patch -Uri "https://api.notion.com/v1/blocks/$parentId/children" -Headers $headers -Body $body | Out-Null
  }
  catch {
    if ($_.Exception.Response -and $_.Exception.Response.GetResponseStream()) {
      $reader = New-Object System.IO.StreamReader($_.Exception.Response.GetResponseStream())
      $resp = $reader.ReadToEnd()
      Write-Output $resp
    }
    throw
  }
}

$children = @(
  @{ object='block'; type='divider'; divider=@{} },
  @{ object='block'; type='heading_2'; heading_2=@{ rich_text=@((T 'Dashboard operativo')); color='default'; is_toggleable=$false } },
  @{ object='block'; type='paragraph'; paragraph=@{ rich_text=@((T 'Vista pensada para decidir rapido: que importa hoy, que esta en movimiento, donde hay bloqueo y que sigue.')); color='default' } },
  @{ object='block'; type='callout'; callout=@{ rich_text=@((T 'Uso simple: captura en tablas base, mira el foco, ejecuta y revisa bloqueos.')); color='gray_background'; icon=@{ type='emoji'; emoji='📌' } } },
  @{ object='block'; type='heading_3'; heading_3=@{ rich_text=@((T 'Foco de hoy')); color='default'; is_toggleable=$false } },
  @{ object='block'; type='to_do'; to_do=@{ rich_text=@((T '1 resultado clave del dia')); checked=$false; color='default' } },
  @{ object='block'; type='to_do'; to_do=@{ rich_text=@((T '1 bloqueo a resolver hoy')); checked=$false; color='default' } },
  @{ object='block'; type='to_do'; to_do=@{ rich_text=@((T '1 siguiente paso concreto')); checked=$false; color='default' } },
  @{ object='block'; type='heading_3'; heading_3=@{ rich_text=@((T 'Panel de decision')); color='default'; is_toggleable=$false } },
  @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Ahora: lo que esta activo y merece atencion inmediata.')); color='default' } },
  @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Siguiente: cola corta de lo proximo en entrar.')); color='default' } },
  @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Bloqueos: cosas detenidas por dependencia, decision o energia.')); color='default' } },
  @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Delegado: que esta en manos de Atlas, Hestia, Prometeo o Ares.')); color='default' } },
  @{ object='block'; type='heading_3'; heading_3=@{ rich_text=@((T 'Ritmo semanal')); color='default'; is_toggleable=$false } },
  @{ object='block'; type='numbered_list_item'; numbered_list_item=@{ rich_text=@((T 'Lunes a miercoles: empuje de produccion y negocio.')); color='default' } },
  @{ object='block'; type='numbered_list_item'; numbered_list_item=@{ rich_text=@((T 'Jueves a domingo: entrenamiento, vida personal y mantenimiento.')); color='default' } },
  @{ object='block'; type='numbered_list_item'; numbered_list_item=@{ rich_text=@((T 'Revisiones: 8:00 AM y 7:00 PM para correo, calendario y prioridades.')); color='default' } },
  @{ object='block'; type='heading_3'; heading_3=@{ rich_text=@((T 'Agentes y dueños')); color='default'; is_toggleable=$false } },
  @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Atlas -> router, agenda, email y coordinacion general.')); color='default' } },
  @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Prometeo -> TradeLab, MVP y desbloqueo tecnico.')); color='default' } },
  @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Ares -> entrenamiento, disciplina y carga semanal.')); color='default' } },
  @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Hestia -> hogar y coordinacion domestica.')); color='default' } },
  @{ object='block'; type='heading_3'; heading_3=@{ rich_text=@((T 'Reglas del tablero')); color='default'; is_toggleable=$false } },
  @{ object='block'; type='toggle'; toggle=@{ rich_text=@((T 'Estados recomendados')); color='default'; children=@(
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Inbox -> entro pero aun no se decide.')); color='default' } },
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Definir -> requiere aclarar alcance o criterio.')); color='default' } },
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Listo -> listo para ejecutar.')); color='default' } },
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'En progreso -> ya se esta haciendo.')); color='default' } },
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'En espera o Bloqueado -> detenido por alguien o algo.')); color='default' } },
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Hecho -> cerrado y fuera del foco.')); color='default' } }
    ) } },
  @{ object='block'; type='toggle'; toggle=@{ rich_text=@((T 'Prioridad recomendada')); color='default'; children=@(
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Alta -> mueve resultado o evita dano.')); color='default' } },
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Media -> importante pero no urgente.')); color='default' } },
      @{ object='block'; type='bulleted_list_item'; bulleted_list_item=@{ rich_text=@((T 'Baja -> mantenimiento o nice to have.')); color='default' } }
    ) } },
  @{ object='block'; type='heading_3'; heading_3=@{ rich_text=@((T 'Plantilla rapida de captura')); color='default'; is_toggleable=$false } },
  @{ object='block'; type='quote'; quote=@{ rich_text=@((T '[Area] | [Resultado esperado] | [Responsable] | [Estado] | [Prioridad] | [Siguiente paso]')); color='default' } }
)

Append-Children -parentId $pageId -children $children
Write-Output 'OK'
