import os

from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(test_dir, 'test_data', 'result1.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.json')
    file2 = os.path.join(test_dir, 'test_data', 'file2.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2) == result


def test_reverse_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(os.path.dirname(__file__), 'test_data', 
                               'result2.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.json')
    file2 = os.path.join(test_dir, 'test_data', 'file2.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file2, file1) == result

def test_alternate_generate_diff():
    test_dir = os.path.dirname(__file__)
    result_file = os.path.join(os.path.dirname(__file__), 'test_data', 
                               'result3.txt')
    file1 = os.path.join(test_dir, 'test_data', 'file1.json')
    file2 = os.path.join(test_dir, 'test_data', 'file3.json')
    with open(result_file, encoding='utf-8') as result:
        result = result.read()
    assert generate_diff(file1, file2) == result