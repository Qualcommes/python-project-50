import os

from gendiff import generate_diff

# ================== JSON ===========================================


def test_json_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result1.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.json')
    file2 = os.path.join(test_dir, 'test_data', 'file2.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2) == result


def test_json_reverse_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result2.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.json')
    file2 = os.path.join(test_dir, 'test_data', 'file2.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file2, file1) == result


def test_json_alternate_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result3.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.json')
    file2 = os.path.join(test_dir, 'test_data', 'file3.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2) == result


def test_json_recursive_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result4.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file4.json')
    file2 = os.path.join(test_dir, 'test_data', 'file5.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2) == result


def test_json_recursive_plain_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result5.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file4.json')
    file2 = os.path.join(test_dir, 'test_data', 'file5.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2, format_name="plain") == result


def test_json_format_json_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result6.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.json')
    file2 = os.path.join(test_dir, 'test_data', 'file2.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2, format_name="json") == result


def test_json_format_recursive_json_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result7.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file4.json')
    file2 = os.path.join(test_dir, 'test_data', 'file5.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2, format_name="json") == result

# ================== YAML ============================================


def test_yaml_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result1.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.yml')
    file2 = os.path.join(test_dir, 'test_data', 'file2.yml')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2) == result


def test_yaml_reverse_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result2.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.yml')
    file2 = os.path.join(test_dir, 'test_data', 'file2.yml')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file2, file1) == result


def test_yaml_alternate_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result3.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.yml')
    file2 = os.path.join(test_dir, 'test_data', 'file3.yml')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2) == result


def test_yaml_recursive_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result4.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file4.yaml')
    file2 = os.path.join(test_dir, 'test_data', 'file5.yaml')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2) == result


def test_yaml_recursive_plain_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result5.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file4.yaml')
    file2 = os.path.join(test_dir, 'test_data', 'file5.yaml')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2, 'plain') == result


def test_json_format_yaml_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result6.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.yml')
    file2 = os.path.join(test_dir, 'test_data', 'file2.yml')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2, format_name="json") == result


def test_json_format_recursive_yaml_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result7.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file4.yaml')
    file2 = os.path.join(test_dir, 'test_data', 'file5.yaml')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2, format_name="json") == result