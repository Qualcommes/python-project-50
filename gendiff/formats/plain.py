def to_string(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def plain(diff_tree, parent_path=""):
    lines = []

    for node in diff_tree:
        key = node["key"]
        type_ = node["type"]
        property_path = f"{parent_path}{key}"

        if type_ == "added":
            val = to_string(node["value"])
            lines.append(f"Property '{property_path}'"
                         f" was added with value: {val}")
        elif type_ == "removed":
            lines.append(f"Property '{property_path}' was removed")
        elif type_ == "changed":
            old_val = to_string(node["old_value"])
            new_val = to_string(node["new_value"])
            lines.append(f"Property '{property_path}' was updated."
                         f" From {old_val} to {new_val}")
        elif type_ == "nested":
            lines.append(plain(node["children"], f"{property_path}."))
            
    result = "\n".join(lines)
    return f"{result}"