import argparse
import json


def generate_diff(file_path1: str, file_path2: str) -> str:
    with open(file_path1, encoding='utf-8') as file:
        file1 = json.load(file)
    with open(file_path2, encoding='utf-8') as file:
        file2 = json.load(file)
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


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', 
                        help="set format of output")

    args = parser.parse_args()
    
    # обработка
    print(f"Comparing {args.first_file} and {args.second_file}...")
    result = generate_diff(args.first_file, args.second_file)
    print(result)
        

if __name__ == "__main__":
    main()