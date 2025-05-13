import json
import os

from gendiff.formatters.plain import format_value
from gendiff.generate_diff import (
    compute_diff,
    generate_diff,
    load_file,
)
from gendiff.load_json import load_json
from gendiff.load_yaml import load_yaml


def create_test_files():
    yaml_content = "key1: value1\nkey2: value2"
    json_content = {'key1': 'value1', 'key3': 'value3'}

    with open('test1.yaml', 'w') as f:
        f.write(yaml_content)
    
    with open('test2.json', 'w') as f:
        json.dump(json_content, f)


def remove_test_files():
    os.remove('test1.yaml')
    os.remove('test2.json')


def test_load_file():
    create_test_files()  

    yaml_content = {'key1': 'value1', 'key2': 'value2'}
    json_content = {'key1': 'value1', 'key3': 'value3'}

    assert load_yaml('test1.yaml') == yaml_content
    assert load_json('test2.json') == json_content

    try:
        load_file('test.txt')
    except ValueError as e:
        assert str(e) == "Unsupported file format"

    remove_test_files()  


def test_compute_diff():
    data1 = {'key1': 'value1', 'key2': 'value2'}
    data2 = {'key1': 'value1', 'key3': 'value3'}

    expected_diff = [
        {'key': 'key1', 'type': 'unchanged', 'value': 'value1'},
        {'key': 'key2', 'type': 'removed', 'old_value': 'value2'},
        {'key': 'key3', 'type': 'added', 'new_value': 'value3'}
    ]

    assert compute_diff(data1, data2) == expected_diff


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(False) == 'false'
    assert format_value(None) == 'null'
    assert format_value(42) == 42
    assert format_value("test") == "test"


def test_stylish():
    create_test_files() 

    expected_output = "{\n" \
                      "    key1: value1\n" \
                      "  - key2: value2\n" \
                      "  + key3: value3\n" \
                      "}"

    assert generate_diff('test1.yaml', 'test2.json') == expected_output
    
    remove_test_files() 


def test_generate_diff():
    create_test_files()  

    expected_diff = "{\n" \
                    "    key1: value1\n" \
                    "  - key2: value2\n" \
                    "  + key3: value3\n" \
                    "}"

    assert generate_diff('test1.yaml', 'test2.json') == expected_diff

    remove_test_files()  


def run_tests():
    test_load_file()
    test_compute_diff()
    test_format_value()
    test_stylish()
    test_generate_diff()


run_tests()
