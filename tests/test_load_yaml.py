import os

from gendiff.load_yaml import load_yaml, parse_yaml


def test_load_simple_yaml():
  
    yaml_file = 'test_file.yaml'
    with open(yaml_file, 'w') as f:
        f.write("key1: value1\nkey2: value2\n\nkey3: value3\n")

    data = load_yaml(yaml_file)

    expected_data = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }
    assert data == expected_data

    os.remove(yaml_file)


if __name__ == "__main__":
    test_load_simple_yaml()

