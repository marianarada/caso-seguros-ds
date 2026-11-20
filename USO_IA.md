# USO DE INTELIGENCIA ARTIFICIAL

**Proyecto:** Caso Seguros — Prueba Técnica de Ciencia de Datos  
**Fecha:** Noviembre 2026

---

## 1. Herramientas utilizadas

Se utilizó Claude (Anthropic) como asistente de inteligencia artificial a través
de dos agentes con roles diferenciados, configurados mediante prompts de sistema
elaborados por la autora antes de iniciar el proyecto.

---

## 2. Agentes configurados

### Agente 1 — Asistente GitHub y DevOps

Configurado para acompañar la creación y mantenimiento del repositorio: estructura
de carpetas, configuración del entorno virtual, archivo `.gitignore`, `README.md`,
`requirements.txt`, commits y sincronización con GitHub. El agente no tomó
decisiones sobre la arquitectura del proyecto; su rol fue orientar la ejecución
técnica paso a paso y diagnosticar errores de entorno y terminal.

### Agente 2 — Científico de Datos

Configurado para acompañar las decisiones metodológicas del análisis: EDA,
preparación de datos, selección de modelos, evaluación y documentación técnica.
El prompt instruyó explícitamente al agente a no avanzar sin revisar la coherencia
de cada etapa, no recomendar modelos sin justificación y no presentar conclusiones
que los datos no respalden.

---

## 3. Dinámica de trabajo

El desarrollo no fue delegado a la IA. La dinámica fue iterativa y crítica:
la autora planteaba el problema o revisaba los resultados, la IA proponía una
estructura o un fragmento de código, y la autora evaluaba, ajustaba o descartaba
según su criterio antes de continuar.

Los notebooks se construyeron sección por sección, no de una sola vez. En cada
etapa se revisaron los resultados intermedios y se tomaron decisiones explícitas
sobre qué conservar, qué corregir y qué descartar.

---

## 4. Decisiones tomadas por la autora

- **Definición de cliente activo:** Se analizaron las bases disponibles y se
  establecieron los límites temporales considerando únicamente las pólizas vigentes
  al 31 de diciembre de 2025, excluyendo el histórico general.

- **Selección del modelo de churn:** Se eligió Regresión Logística como modelo
  base por su interpretabilidad, y XGBoost como modelo alternativo por su
  crecimiento level-wise, que produce árboles más equilibrados y reduce el riesgo
  de sobreajuste en contextos con baja tasa de churn, frente a LightGBM que
  resultaba menos adecuado dado el volumen de datos disponible.

- **Número de segmentos:** Aunque el modelo K-Means sugería 6 segmentos como
  óptimo, se decidió trabajar con 5 porque la diferencia entre el segmento 5 y 6
  no era estadísticamente significativa ni accionable para el equipo de Mercadeo.

- **Correcciones durante el desarrollo:** Se identificaron y corrigieron errores
  como tipos de variables mal asignados, el valor de prima del SOAT que arrojaba
  cero en la Sección 1, y variables que introducían sesgo en los modelos. En cada
  caso la autora tomó la decisión de corregir, excluir o transformar la variable
  antes de continuar.

---

## 5. Qué se tomó y qué se descartó

| Elemento | Decisión |
|---|---|
| Estructura del código por etapas | Tomado — permitió revisar cada paso antes de avanzar |
| Sugerencia de 6 segmentos en K-Means | Descartado — se usaron 5 por criterio de interpretabilidad |
| Variables con tipos incorrectos | Corregidas por instrucción explícita de la autora |
| Resultado de prima SOAT = 0 | Identificado como error y corregido |
| Variables que sesgaban resultados | Excluidas por decisión de la autora tras revisar el impacto |

---

## 6. Limitaciones del uso de IA

El código generado requirió revisión y ajuste continuo. La IA no tuvo acceso
directo a los datos y no ejecutó ningún notebook: todo el código fue ejecutado,
validado e interpretado por la autora. Las conclusiones del análisis son propias
y no fueron generadas automáticamente.