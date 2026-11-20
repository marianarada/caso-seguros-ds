# =============================================================
# SCRIPT MAESTRO — caso-seguros-ds
# Ejecuta todos los notebooks en orden y genera los outputs
# Uso: python run_all.py
# =============================================================

import subprocess
import sys
from pathlib import Path

NOTEBOOKS = [
    "notebooks/00_calidad_datos.ipynb",
    "notebooks/01_valor_cliente.ipynb",
    "notebooks/02_riesgo_fuga.ipynb",
    "notebooks/03_segmentacion.ipynb",
    "notebooks/04_analisis_texto.ipynb",
    "notebooks/05_campana_retencion.ipynb",
]

def run_notebook(path: str):
    print(f"\n{'='*60}")
    print(f"▶ Ejecutando: {path}")
    print(f"{'='*60}")
    result = subprocess.run(
        [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            path
        ],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"✅ {path} — OK")
    else:
        print(f"❌ {path} — ERROR")
        print(result.stderr)
        sys.exit(1)

if __name__ == "__main__":
    print("🚀 Iniciando ejecución del proyecto caso-seguros-ds")
    for nb in NOTEBOOKS:
        run_notebook(nb)
    print("\n✅ Todos los notebooks ejecutados correctamente.")
    print("📁 Outputs generados en: outputs/")