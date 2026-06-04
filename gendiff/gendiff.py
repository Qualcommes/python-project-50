from .parser import parser


def generate_diff(file_path1: str, file_path2: str) -> str:
    parsed = parser(file_path1, file_path2)
    file1 = parsed[0]
    file2 = parsed[1]
    set1 = set(file1)
    set2 = set(file2)
    difference = set1 - set2
    intersection = set1 & set2
    plus = set2 - set1
    all_keys = sorted(set1 | set2)
    result = '{\n'
    for key in all_keys:
        if key in difference:
            result += '  - ' + key + ': ' + str(file1[key]).lower() + '\n'
            continue
        elif key in intersection:
            if file1[key] == file2[key]:
                result += '    ' + key + ': ' + str(file1[key]).lower() + '\n'
            else:
                result += '  - ' + key + ': ' + str(file1[key]).lower() + \
                '\n  + ' + key + ': ' + str(file2[key]).lower() + '\n'
            continue
        elif key in plus:
            result += '  + ' + key + ': ' + str(file2[key]).lower() + '\n'
            continue
    result += '}'
    return result