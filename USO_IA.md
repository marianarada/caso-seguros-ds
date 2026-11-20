# USO DE INTELIGENCIA ARTIFICIAL

**Proyecto:** Caso Seguros — Prueba Técnica de Ciencia de Datos  
**Fecha:** Noviembre 2026  
**Herramienta:** Claude (Anthropic)

---

## 1. Contexto general

Durante el desarrollo de este proyecto se utilizó Claude (Anthropic) como
asistente de inteligencia artificial. El uso no fue pasivo: se configuraron
dos agentes con roles específicos mediante prompts de sistema elaborados por
la autora, y la interacción fue iterativa — la IA proponía, la autora evaluaba,
ajustaba y decidía.

En ningún caso se delegó el análisis completo a la IA. Los notebooks se
construyeron sección por sección, revisando resultados intermedios antes de
avanzar. Las conclusiones, decisiones metodológicas y criterios de exclusión
son propios.

---

## 2. Agentes configurados y prompts utilizados

### Agente 1 — Senior Software Engineer / GitHub Specialist / DevOps Mentor

**Propósito:** Acompañar la creación y mantenimiento del repositorio, configuración
del entorno de desarrollo y resolución de errores técnicos de Git y VS Code.

**Prompt de sistema utilizado:**

> Actúa como un Senior Software Engineer especializado en Python, Git, GitHub,
> Visual Studio Code, desarrollo de proyectos de ciencia de datos y buenas
> prácticas de ingeniería de software.
>
> Tu responsabilidad es acompañarme durante todo el ciclo de desarrollo de mi
> proyecto de ciencia de datos, desde la creación del repositorio hasta su
> publicación, documentación y mantenimiento.
>
> Cuando te presente un problema: analiza el contexto antes de proponer una
> solución, identifica la causa probable, solicita información cuando no tengas
> suficiente, explícame qué está fallando y por qué, proporciona instrucciones
> paso a paso e incluye los comandos exactos que debo ejecutar.
>
> No cambies la arquitectura del proyecto sin justificarlo. No propongas
> soluciones innecesariamente complejas. No me des diez instrucciones
> simultáneas cuando podemos solucionar un problema por etapas.

**Uso concreto:**
- Configuración del repositorio local y conexión con GitHub
- Definición de la estructura de carpetas (`data/`, `notebooks/`, `outputs/`,
  `reports/`, `figures/`, `src/`)
- Configuración del `.gitignore` para excluir datos crudos y el entorno virtual
- Creación del `README.md` con instrucciones de ejecución
- Diagnóstico de errores de terminal (por ejemplo, cuando el `.gitignore` fue
  pegado en la terminal en lugar del archivo, ejecutando cada línea como comando)
- Resolución del error "Invalid Notebook" en GitHub por archivos `.ipynb` vacíos
- Orientación en commits, push y sincronización con `origin/main`

---

### Agente 2 — Principal Data Scientist / Machine Learning Engineer / MLOps Expert

**Propósito:** Acompañar las decisiones metodológicas y técnicas del análisis de
datos: EDA, preparación, modelado, evaluación e interpretación de resultados.

**Prompt de sistema utilizado:**

> Actúa como un Principal Data Scientist con amplia experiencia en estadística,
> econometría, análisis exploratorio de datos, inteligencia artificial, machine
> learning, deep learning, feature engineering, model evaluation y MLOps.
>
> Tu responsabilidad es acompañarme en todas las etapas metodológicas y técnicas
> de mi proyecto de ciencia de datos. No quiero que simplemente escribas código
> o ejecutes algoritmos. Quiero que actúes como un científico de datos senior
> que evalúa críticamente mis decisiones, me orienta cuando no conozco el
> siguiente paso y me ayuda a construir soluciones técnicamente sólidas.
>
> Trabajaremos por etapas. No debes avanzar automáticamente a la siguiente etapa
> sin revisar si la anterior tiene coherencia. Si mi planteamiento es incorrecto,
> debes decírmelo y proponer una alternativa. Si existen varias metodologías
> válidas, compara sus ventajas y limitaciones.
>
> Nunca inventes resultados. No interpretes resultados que no hayas visto. No
> confundas correlación con causalidad. No permitas data leakage. No presentes
> conclusiones que los datos no respalden.

**Uso concreto:**
- Construcción de la base de clientes activos (Sección 0)
- Auditoría de calidad de los 12 archivos CSV
- Formulación y estimación del valor del cliente (Sección 1)
- Definición de fuga y construcción del modelo de churn (Sección 2)
- Segmentación de clientes con K-Means (Sección 3)
- Modelado de temas y sentimiento en comentarios de experiencia (Sección 4)
- Evaluación causal de la campaña de retención (Sección 5)

---

## 3. Dinámica de trabajo

La interacción con la IA fue iterativa y crítica. El flujo general fue:

1. La autora planteaba el problema o revisaba resultados intermedios
2. La IA proponía una estructura de código o un enfoque metodológico
3. La autora ejecutaba el código, revisaba los resultados y decidía si ajustar,
   corregir o descartar
4. Se le indicaba a la IA qué cambiar y por qué, antes de continuar

Esto implicó múltiples rondas de corrección por sección. No se trabajó con un
notebook completo de una sola vez.

---

## 4. Decisiones tomadas por la autora

**Sección 0 — Calidad de datos:**
Se analizaron las bases disponibles y se establecieron los límites temporales
considerando únicamente las pólizas vigentes al 31 de diciembre de 2025. Se
excluyó el histórico general para evitar contar como activos a clientes que
habían cancelado antes de la fecha de corte.

**Sección 2 — Modelo de churn:**
Se eligió Regresión Logística como modelo base por su interpretabilidad y
facilidad de calibración. Como modelo alternativo se seleccionó XGBoost por
su crecimiento level-wise, que produce árboles más equilibrados y reduce el
riesgo de sobreajuste en contextos con baja tasa de churn. Se descartó LightGBM
porque su crecimiento leaf-wise, aunque más rápido, era menos adecuado dado el
volumen de registros disponible. Esta decisión se tomó con base en experiencia
previa en proyectos similares y conocimiento del comportamiento de ambos algoritmos.

**Sección 3 — Número de segmentos:**
El modelo K-Means con el criterio del codo y el Silhouette Score sugería 6
segmentos como óptimo. Se decidió trabajar con 5 porque la diferencia entre
el segmento 5 y el 6 no era estadísticamente significativa ni producía un grupo
accionable adicional para el equipo de Mercadeo.

**Correcciones durante el desarrollo:**
- Se identificaron variables con tipos de datos incorrectos y se instruyó a la
  IA para corregirlos antes de continuar el análisis
- El valor de prima del SOAT arrojaba cero en la Sección 1, lo cual fue
  identificado como un error de cálculo y corregido
- Se tomaron decisiones explícitas de excluir variables que introducían sesgo
  en los modelos, evaluando su impacto antes de proceder

---

## 5. Qué se tomó y qué se descartó

| Elemento | Decisión |
|---|---|
| Estructura del código por etapas | Tomado — permitió revisar cada paso antes de avanzar |
| Sugerencia de 6 segmentos en K-Means | Descartado — se trabajó con 5 por criterio de interpretabilidad y accionabilidad |
| Variables con tipos de datos incorrectos | Corregidas por instrucción explícita de la autora tras revisar los resultados |
| Prima SOAT = 0 en Sección 1 | Identificado como error por la autora y corregido |
| Variables que sesgaban los modelos | Excluidas por decisión de la autora tras evaluar su impacto en los resultados |
| LightGBM como modelo de churn | Descartado — se prefirió XGBoost por mejor comportamiento con datos desbalanceados |

---

## 6. Lo que la IA no hizo

- No ejecutó ningún notebook
- No tomó decisiones metodológicas de forma autónoma

Todo el código fue ejecutado, validado e interpretado por la autora. Las
conclusiones son propias y están sustentadas en los resultados obtenidos.
