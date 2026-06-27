from .formatter import format
from .parser import load_file


def build_diff(data1: dict, data2: dict) -> list:
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key not in data1:
            diff.append({
                "key": key,
                "type": "added",
                "value": data2[key]
            })
        elif key not in data2:
            diff.append({
                "key": key,
                "type": "removed",
                "value": data1[key]
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                "key": key,
                "type": "nested",
                "children": build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({
                "key": key, 
                "type": "unchanged", 
                "value": data1[key]
            })
        else:
            diff.append({
                "key": key,
                "type": "changed",
                "old_value": data1[key],
                "new_value": data2[key]
            })
    return diff


def generate_diff(file_path1: str, file_path2: str, 
                  format_name='stylish') -> str:
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)
    
    diff_tree = build_diff(data1, data2)
    return format(diff_tree, format_style=format_name)



