import json


def json_formatter(diff_tree, parent_path=""):
    lines = []

    for node in diff_tree:
        key = node["key"]
        type_ = node["type"]
        property_path = f"{parent_path}/{key}"

        if type_ == "added":
            # Передаем node["value"] как есть, без to_string()
            lines.append({
                "op": "add", 
                "path": property_path, 
                "value": node["value"]
            })
        elif type_ == "removed":
            lines.append({
                "op": "remove", 
                "path": property_path
            })
        elif type_ == "changed":
            lines.append({
                "op": "replace", 
                "path": property_path, 
                "value": node["new_value"]
            })
        elif type_ == "nested":
            nested_lines = json_formatter(node["children"], property_path)
            lines.extend(nested_lines)

    return lines


def render_json(diff_tree):
    raw_patch = json_formatter(diff_tree)
    return json.dumps(raw_patch, indent=2, ensure_ascii=False)