import pytest
from formatters.stylish import stylish, format_value


def test_format_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value(False) == 'false'
    assert format_value(123) == 123 
    assert format_value('string') == 'string'


def test_stylish_added():
    diff = [
        {'key': 'common.setting1', 'type': 'added', 'new_value': 'value1'},
        {'key': 'common.setting2', 'type': 'added', 'new_value': 42},
    ]
    expected_output = (
        "  + common.setting1: value1\n"
        "  + common.setting2: 42"
    )
    assert stylish(diff) == expected_output


def test_stylish_removed():
    diff = [
        {'key': 'common.setting1', 'type': 'removed', 'old_value': 'value1'},
        {'key': 'common.setting2', 'type': 'removed', 'old_value': 42},
    ]
    expected_output = (
        "  - common.setting1: value1\n"
        "  - common.setting2: 42"
    )
    assert stylish(diff) == expected_output


def test_stylish_modified():
    diff = [
        {'key': 'common.setting1', 'type': 'modified', 'old_value': 'old_value1', 'new_value': 'new_value1'},
        {'key': 'common.setting2', 'type': 'modified', 'old_value': 10, 'new_value': 20},
    ]
    expected_output = (
        "  - common.setting1: old_value1\n"
        "  + common.setting1: new_value1\n"
        "  - common.setting2: 10\n"
        "  + common.setting2: 20"
    )
    assert stylish(diff) == expected_output


def test_stylish_nested():
    diff = [
        {
            'key': 'common',
            'type': 'nested',
            'children': [
                {'key': 'setting1', 'type': 'added', 'new_value': 'value1'},
                {'key': 'setting2', 'type': 'removed', 'old_value': 'value2'},
            ]
        },
        {'key': 'common.setting3', 'type': 'modified', 'old_value': 'old_value3', 'new_value': 'new_value3'},
    ]
    expected_output = (
        "    common: {\n"
        "      + setting1: value1\n"
        "      - setting2: value2\n"
        "    }\n"
        "  - common.setting3: old_value3\n"
        "  + common.setting3: new_value3"
    )
    assert stylish(diff) == expected_output


def test_stylish_unchanged():
    diff = [
        {'key': 'common.setting1', 'type': 'unchanged', 'value': 'value1'},
        {'key': 'common.setting2', 'type': 'unchanged', 'value': 42},
    ]
    expected_output = (
        "    common.setting1: value1\n"
        "    common.setting2: 42"
    )
    assert stylish(diff) == expected_output
