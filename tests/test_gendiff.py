import os

from gendiff.generate_diff import generate_diff

filepath1 = os.path.join('files', 'file1.json')
filepath2 = os.path.join('files', 'file2.json')


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
    test_generate_diff()
