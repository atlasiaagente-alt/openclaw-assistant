# Sistema base — factura mensual al proveedor

Fecha: 2026-03-27

## Objetivo
Dejar listo el esqueleto para que, cuando Gustavo comparta la plantilla, se pueda:
1. recordar a tiempo
2. calcular horas/valor base
3. prearmar borrador

## Reglas conocidas
- Zona horaria: Colombia
- Días laborables: lunes a viernes
- Festivos colombianos: no se trabajan
- Jornada: 8 horas/día
- Tarifa recordada: **USD 38/hora**

## Cálculo base provisional
- Valor diario: **USD 304**
- Fórmula mensual provisional:
  - `días hábiles trabajados x 8 x 38`

## Pendientes para automatizar bien
- Plantilla real de factura
- Confirmar si la tarifa sigue siendo exactamente USD 38/hora
- Definir formato de salida (PDF, DOCX, Google Docs, Notion, etc.)
- Definir si hay campos variables: número de factura, NIT, razón social, fechas de corte, impuestos, moneda final

## Siguiente paso concreto
Cuando llegue la plantilla:
- mapear campos
- crear checklist de llenado
- dejar un borrador reusable

## Idea de automatización posterior
- Recordatorio **3 a 5 días antes de fin de mes**
- Si existe plantilla estructurada, prearmar borrador automático con:
  - mes
  - rango de fechas
  - días laborables
  - horas
  - subtotal
