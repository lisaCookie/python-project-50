from gendiff.formatters.stylish import str_format, stylish

def test_str_format():
    assert str_format(None) == 'null'
    assert str_format(True) == 'true'
    assert str_format(False) == 'false'
    assert str_format('hello') == 'hello'
    assert str_format(42) == '42'
    sample_dict = {'a': 1, 'b': {'c': None}}
    result = str_format(sample_dict, depth=2)
    assert 'a: 1' in result
    assert 'b:' in result
    assert 'c: null' in result

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
    expected = (
        "    key1: {\n"
        "        key2: value2\n"
        "    }"
    )
    assert result == expected


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
    assert result == expected