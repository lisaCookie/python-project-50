import os

from gendiff.load_json import load_json

filepath1 = os.path.join('files', 'file1.json')
filepath2 = os.path.join('files', 'file2.json')


def test_load_json():
    assert load_json(filepath1) == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "192.168.12.42",
        "follow": False
    }
    assert load_json(filepath2) == {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }
    try:
        load_json('non_existing.json')
        assert False
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    test_load_json()
