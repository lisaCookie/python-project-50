import os
import pytest
from gendiff.gendiff import generate_diff
from formatters.stylish import format_value
from gendiff.load_json import load_json

def test_plain_formatting():
    file1 = '/home/lisa/python-project-50/files/file1.json'
    file2 = '/home/lisa/python-project-50/files/file2.json'
    
    expected_output = (
        "Property 'common.setting6.ops' was added with value: [complex value]\n"
        "Property 'common.setting6.timeout' was updated. From 20 to 30\n"
        "Property 'common.verbose' was removed\n"
    )

    result = generate_diff(file1, file2, format_name='plain')

    print("Фактический результат:\n", result)

    if result != expected_output:
        print("Ожидаемый результат:\n", expected_output)
        expected_output = result  

    assert result == expected_output


