import json
import os

import yaml


def load_file(file_path: str):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext in ('.yml', '.yaml'):
        with open(file_path, encoding='utf-8') as file:
            return yaml.safe_load(file) or {}
    elif ext == '.json':
        with open(file_path, encoding='utf-8') as file:
            return json.load(file) or {}
    else:
        raise ValueError(f"Unsupported file format: {ext}")
