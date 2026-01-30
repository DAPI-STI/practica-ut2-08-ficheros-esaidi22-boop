from __future__ import annotations
from pathlib import Path

def _load_phonebook(path: str | Path) -> dict[str, str]:
    path = Path(path)
    phonebook: dict[str, str] = {}
    if not path.exists():
        return phonebook
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",", 1)
            if len(parts) != 2:
                raise ValueError(f"Línea mal formada: {line}")
            name, phone = parts
            phonebook[name.strip()] = phone.strip()
    return phonebook

def _save_phonebook(path: str | Path, phonebook: dict[str, str]) -> None:
    path = Path(path)
    with path.open("w", encoding="utf-8") as f:
        for name, phone in phonebook.items():
            f.write(f"{name},{phone}\n")

def add_contact(path: str | Path, name: str, phone: str) -> None:
    name = name.strip()
    phone = phone.strip()
    if not name or not phone:
        raise ValueError("Nombre y teléfono no pueden estar vacíos")
    phonebook = _load_phonebook(path)
    phonebook[name] = phone
    _save_phonebook(path, phonebook)

def get_phone(path: str | Path, name: str) -> str | None:
    name = name.strip()
    phonebook = _load_phonebook(path)
    return phonebook.get(name)

def remove_contact(path: str | Path, name: str) -> bool:
    name = name.strip()
    phonebook = _load_phonebook(path)
    if name in phonebook:
        del phonebook[name]
        _save_phonebook(path, phonebook)
        return True
    return False

