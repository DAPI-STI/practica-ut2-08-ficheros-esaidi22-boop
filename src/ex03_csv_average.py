"""
EX03 (CSV) · Calcular la media de una columna

Objetivo:
- Leer un CSV con cabecera (primera línea).
- Usar la librería estándar `csv` (recomendado: csv.DictReader).
- Convertir datos a float y calcular una media.

Ejemplo típico:
- Un CSV de calificaciones con columnas: name, average
"""
from __future__ import annotations
from pathlib import Path
import csv

def csv_average(path: str | Path, column: str) -> float:
    """
    Calcula y devuelve la media de la columna numérica `column` en el CSV `path`.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No existe el fichero: {path}")

    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if column not in reader.fieldnames:
            raise ValueError(f"La columna '{column}' no existe en el CSV")

        values = []
        for row in reader:
            try:
                values.append(float(row[column]))
            except ValueError:
                raise ValueError(f"Valor no numérico en la columna '{column}'")

        if not values:
            raise ValueError(f"No hay filas de datos en el CSV")

        return sum(values) / len(values)
