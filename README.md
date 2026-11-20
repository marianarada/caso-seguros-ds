# Caso Seguros — Prueba Técnica de Ciencia de Datos

Valor, fuga, segmentación y retención de clientes en seguros voluntarios.

---

## Requisitos

- Python 3.14+
- Git

---

## Instalación

```bash
git clone https://github.com/marianarada/caso-seguros-ds.git
cd caso-seguros-ds
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Datos

Coloca los 12 archivos CSV en la carpeta `data/`:

```
asesores.csv, campana_retencion_2025.csv, clientes.csv,
coberturas.csv, experiencia.csv, leads.csv,
parametros_financieros.csv, polizas.csv, pqrs.csv,
recaudos.csv, roles_poliza.csv, siniestros.csv
```

## Ejecución

### Opción 1 — Script maestro (reproduce todo)

```bash
python run_all.py
```

### Opción 2 — Notebook por notebook

Abre cada notebook en Jupyter o VS Code y ejecútalo en orden:

| # | Notebook | Sección |
|---|---|---|
| 0 | `notebooks/00_calidad_datos.ipynb` | Base de clientes y calidad de datos |
| 1 | `notebooks/01_valor_cliente.ipynb` | Valor del cliente (CLV) |
| 2 | `notebooks/02_riesgo_fuga.ipynb` | Fuga de clientes |
| 3 | `notebooks/03_segmentacion.ipynb` | Segmentación para la retención |
| 4 | `notebooks/04_analisis_texto.ipynb` | Análisis de comentarios de experiencia |
| 5 | `notebooks/05_campana_retencion.ipynb` | A quién contactar para retener |

## Outputs generados

Los archivos de entrega se guardan automáticamente en `outputs/`:

- `valor_cliente.csv`
- `riesgo_fuga.csv`
- `segmentos.csv`
- `contactos_2026.csv`
- `comentarios_analizados.csv`

## Semilla fija

Todos los modelos usan `SEED = 42` para garantizar reproducibilidad.

## Estructura del repositorio

```
caso-seguros-ds/
├── data/                  # CSVs de entrada (no versionados)
├── notebooks/             # Un notebook por sección
├── outputs/               # CSVs de entrega
├── reports/               # Documentación técnica en PDF
├── figures/               # Gráficas generadas
├── src/                   # Funciones auxiliares
├── run_all.py             # Script maestro
├── requirements.txt       # Dependencias
└── README.md
```

---

## Autora

**Mariana Rada Espitia**

Economista | Especialista en Ciencia de Datos e Inteligencia Artificial

Intereses profesionales:

- Data Science & Machine Learning.
- Business Intelligence.
- Customer Analytics.
- Predictive Modeling.
- Marketing Analytics.
- Data-driven Decision Making.

GitHub: [@marianarada](https://github.com/marianarada)
