"""
EX01 (Texto) · Buscar una palabra en un fichero

Objetivo:
- Practicar la lectura de ficheros de texto usando `open(...)`.
- Normalizar el contenido (minúsculas) y contar coincidencias.

Consejo:
- No hace falta una solución "perfecta" de NLP.
  Con que cuentes palabras separadas por espacios y elimines puntuación básica es suficiente.
"""
from __future__ import annotations

from pathlib import Path
import string


def count_word_in_file(path: str | Path, word: str) -> int:
    if not word or word.strip() == "":
        raise ValueError("La palabra no puede estar vacía")

    path = Path(path)

    text = path.read_text(encoding="utf-8")

    text = text.lower()
    word = word.lower().strip()

    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
    text = text.translate(translator)

    words = text.split()
    return words.count(word)

