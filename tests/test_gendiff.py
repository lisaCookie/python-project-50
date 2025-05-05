import json
import os
from gendiff.gendiff import gendiff  
from gendiff.load_yaml import load_yaml  
from gendiff.load_json import load_json

def test_load_file_json():
    json_file = 'test_file.json'
    with open(json_file, 'w') as f:
        json.dump({"key1": "value1", "key2": "value2"}, f)

    data = load_json(json_file)
    assert data == {"key1": "value1", "key2": "value2"}

    os.remove(json_file)

def test_load_file_yaml():
    yaml_file = 'test_file.yaml'
    with open(yaml_file, 'w') as f:
        f.write("key1: value1\nkey2: value2\n")

    data = load_yaml(yaml_file)
    assert data == {"key1": "value1", "key2": "value2"}

    os.remove(yaml_file)

def test_gendiff_json():
    json_file1 = 'test_file1.json'
    json_file2 = 'test_file2.json'
    with open(json_file1, 'w') as f:
        json.dump({"key1": "value1", "key2": "value2"}, f)
    with open(json_file2, 'w') as f:
        json.dump({"key2": "value2", "key3": "value3"}, f)

    expected_diff = "{\n  - key1: value1\n  + key3: value3\n}"
    diff = gendiff(json_file1, json_file2)
    assert diff == expected_diff

    os.remove(json_file1)
    os.remove(json_file2)

def test_gendiff_yaml():
    yaml_file1 = 'test_file1.yaml'
    yaml_file2 = 'test_file2.yaml'
    with open(yaml_file1, 'w') as f:
        f.write("key1: value1\nkey2: value2\n")
    with open(yaml_file2, 'w') as f:
        f.write("key2: value2\nkey3: value3\n")

    expected_diff = "{\n  - key1: value1\n  + key3: value3\n}"
    diff = gendiff(yaml_file1, yaml_file2)
    assert diff == expected_diff

    os.remove(yaml_file1)
    os.remove(yaml_file2)

if __name__ == "__main__":
    test_load_file_json()
    test_load_file_yaml()
    test_gendiff_json()
    test_gendiff_yaml()
