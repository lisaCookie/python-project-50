import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gendiff.diff import generate_diff, load_json

filepath1 = os.path.join(
    os.path.dirname(__file__), '..', 'gendiff', 'filepath1.json'
)
filepath2 = os.path.join(
    os.path.dirname(__file__), '..', 'gendiff', 'filepath2.json'
)


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


def test_generate_diff():
    result = generate_diff(filepath1, filepath2)
    assert "{\n" in result
    assert "  - follow: False" in result
    assert "  - proxy: 192.168.12.42" in result
    assert "  - timeout: 50" in result
    assert "  + timeout: 20" in result
    assert "  + verbose: True" in result
    assert "    host: hexlet.io" in result

    result_same = generate_diff(filepath1, filepath1)
    assert result_same.strip() == (
        "{\n"
        "    follow: False\n"
        "    host: hexlet.io\n"
        "    proxy: 192.168.12.42\n"
        "    timeout: 50\n"
        "}"
    )


if __name__ == "__main__":
    test_load_json()
    test_generate_diff()