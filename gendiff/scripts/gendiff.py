import argparse
import json


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
    with open(args.first_file, encoding='utf-8') as file:
        file1 = json.load(file)
    with open(args.second_file, encoding='utf-8') as file:
        file2 = json.load(file)
        

if __name__ == "__main__":
    main()