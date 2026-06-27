def to_string(value, depth):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return str(value)

    indent = "    " * depth
    closing_indent = "    " * (depth)
    
    lines = []
    for key, val in value.items():
        lines.append(f"{indent}    {key}: {to_string(val, depth + 1)}")
        
    result = "\n".join(lines)
    return f"{{\n{result}\n{closing_indent}}}"


def stylish(diff_tree, depth=1):
    indent_size = depth * 4
    current_indent = " " * (indent_size - 2)
    
    lines = []
    for node in diff_tree:
        key = node["key"]
        type_ = node["type"]
        
        if type_ == "added":
            val = to_string(node['value'], depth)
            lines.append(f"{current_indent}+ {key}: {val}")
        elif type_ == "removed":
            val = to_string(node['value'], depth)
            lines.append(f"{current_indent}- {key}: {val}")
        elif type_ == "unchanged":
            val = to_string(node['value'], depth + 1)
            lines.append(f"{current_indent}  {key}: {val}")
        elif type_ == "changed":
            val1 = to_string(node['old_value'], depth)
            val2 = to_string(node['new_value'], depth)
            lines.append(f"{current_indent}- {key}: {val1}")
            lines.append(f"{current_indent}+ {key}: {val2}")
        elif type_ == "nested":
            val = stylish(node['children'], depth + 1)
            lines.append(f"{current_indent}  {key}: {val}")
            
    result = "\n".join(lines)
    closing_indent = "    " * (depth - 1)
    return f"{{\n{result}\n{closing_indent}}}"