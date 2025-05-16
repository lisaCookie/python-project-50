from gendiff.formatters.stylish import format_value, stylish


def test_format_value():
    result = format_value({'key1': 'value1', 'key2': 'value2'})
    expected = "{\n    key1: value1,\n    key2: value2\n}"
    assert result == expected


def test_stylish_added():
    diff = [{'key': 'key1', 'type': 'added', 'new_value': 'value1'}]
    result = stylish(diff)
    expected = "  + key1: value1"
    assert result == expected


def test_stylish_removed():
    diff = [{'key': 'key1', 'type': 'removed', 'old_value': 'value1'}]
    result = stylish(diff)
    expected = "  - key1: value1"
    assert result == expected


def test_stylish_modified():
    diff = [
        {
            'key': 'key1',
            'type': 'modified',
            'old_value': 'old_value',
            'new_value': 'new_value'
        }
    ]
    result = stylish(diff)
    expected = (
        "  - key1: old_value\n"
        "  + key1: new_value"
    )
    assert result == expected


def test_stylish_nested():
    diff = [
        {'key': 'key1', 'type': 'nested', 'children': [
            {'key': 'key2', 'type': 'unchanged', 'value': 'value2'}
        ]}
    ]
    result = stylish(diff)
    expected = "    key1: {\n        key2: value2\n    }"
    assert result.strip() == expected.strip()


def test_stylish_unchanged():
    diff = [{'key': 'key1', 'type': 'unchanged', 'value': 'value1'}]
    result = stylish(diff)
    expected = "    key1: value1"
    assert result == expected


def test_stylish_complex():
    diff = [
        {'key': 'key1', 'type': 'added', 'new_value': 'value1'},
        {'key': 'key2', 'type': 'removed', 'old_value': 'value2'},
        {
            'key': 'key3',
            'type': 'modified',
            'old_value': 'old_value',
            'new_value': 'new_value'
        },
        {
            'key': 'key4',
            'type': 'nested',
            'children': [
                {'key': 'key5', 'type': 'unchanged', 'value': 'value5'}
            ]
        }
    ]
    
    result = stylish(diff)
    expected = (
        "  + key1: value1\n"
        "  - key2: value2\n"
        "  - key3: old_value\n"
        "  + key3: new_value\n"
        "    key4: {\n"
        "        key5: value5\n"
        "    }"
    )
    assert result.strip() == expected.strip()