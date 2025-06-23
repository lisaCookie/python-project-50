import json
import os

from gendiff.generate_diff import generate_diff


def cleanup_files(filenames):
    for filename in filenames:
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass


def test_generate_diff_json():
    filenames = ['file1.json', 'file2.json']
    try:
        with open('file1.json', 'w') as f:
            json.dump({'key1': 'value1', 'key2': 'value2'}, f)
        with open('file2.json', 'w') as f:
            json.dump({'key1': 'value1', 'key2': 'value3', 'key3': 'value4'}, f)

        result = generate_diff('file1.json', 'file2.json', 'stylish')
        expected = (
            "{\n"
            "    key1: value1\n"
            "  - key2: value2\n"
            "  + key2: value3\n"
            "  + key3: value4\n"
            "}"
        )
        assert result == expected
    finally:
        cleanup_files(filenames)


def test_generate_diff_yaml():
    filenames = ['file1.yaml', 'file2.yaml']
    try:
        with open('file1.yaml', 'w') as f:
            f.write("key1: value1\nkey2: value2")
        with open('file2.yaml', 'w') as f:
            f.write("key1: value1\nkey2: value3\nkey3: value4")

        result = generate_diff('file1.yaml', 'file2.yaml', 'stylish')
        expected = (
            "{\n"
            "    key1: value1\n"
            "  - key2: value2\n"
            "  + key2: value3\n"
            "  + key3: value4\n"
            "}"
        )
        assert result.strip() == expected.strip()
    finally:
        cleanup_files(filenames)


def test_generate_diff_plain_format():
    filenames = ['file1.json', 'file2.json']
    try:
        with open('file1.json', 'w') as f:
            json.dump({'key1': 'value1'}, f)
        with open('file2.json', 'w') as f:
            json.dump({'key1': 'value1', 'key2': 'value2'}, f)

        result = generate_diff('file1.json', 'file2.json', 'plain')
        expected = "Property 'key2' was added with value: 'value2'"  
        assert result == expected
    finally:
        cleanup_files(filenames)


def test_generate_diff_json_format():
    filenames = ['file1.json', 'file2.json']
    try:
        with open('file1.json', 'w') as f:
            json.dump({'key1': 'value1'}, f)
        with open('file2.json', 'w') as f:
            json.dump({'key1': 'value1', 'key2': 'value2'}, f)

        result = generate_diff('file1.json', 'file2.json', 'json')
        expected = json.dumps([
            {'key': 'key1', 'type': 'unchanged', 'value': 'value1'},
            {'key': 'key2', 'type': 'added', 'new_value': 'value2'}
        ], indent=4)
        assert result == expected
    finally:
        cleanup_files(filenames)