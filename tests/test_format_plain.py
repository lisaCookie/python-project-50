import json
import os

from formatters.plain import format_value
from gendiff.load_json import load_json
from formatters.plain import format_plain

import pytest

def test_format_plain_added():
    diff = [
        {'key': 'common.setting1', 'type': 'added', 'new_value': 'value1'},
        {'key': 'common.setting2', 'type': 'added', 'new_value': 42},
    ]
    expected_output = (
        "Property 'common.setting1' was added with value: value1\n"
        "Property 'common.setting2' was added with value: 42"
    )
    assert format_plain(diff) == expected_output


def test_format_plain_removed():
    diff = [
        {'key': 'common.setting1', 'type': 'removed'},
        {'key': 'common.setting2', 'type': 'removed'},
    ]
    expected_output = (
        "Property 'common.setting1' was removed\n"
        "Property 'common.setting2' was removed"
    )
    assert format_plain(diff) == expected_output


def test_format_plain_modified():
    diff = [
        {
            'key': 'common.setting1',
            'type': 'modified',
            'old_value': 'old_value1',
            'new_value': 'new_value1'
        },
        {
            'key': 'common.setting2',
            'type': 'modified',
            'old_value': 10,
            'new_value': 20
        },
    ]
    expected_output = (
        "Property 'common.setting1' was updated. From old_value1 to new_value1\n"
        "Property 'common.setting2' was updated. From 10 to 20"
    )
    assert format_plain(diff) == expected_output


def test_format_plain_nested():
    diff = [
        {
            'key': 'common',
            'type': 'nested',
            'children': [
                {'key': 'setting1', 'type': 'added', 'new_value': 'value1'},
                {'key': 'setting2', 'type': 'removed'},
            ]
        },
        {
            'key': 'common.setting3',
            'type': 'modified',
            'old_value': 'old_value3',
            'new_value': 'new_value3'
        },
    ]
    expected_output = (
        "Property 'common.setting1' was added with value: value1\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From old_value3 to new_value3"
    )
    assert format_plain(diff) == expected_output


def test_format_value():
    assert format_value(None) == 'null'
    assert format_value(True) == 'true'
    assert format_value(False) == 'false'
    assert format_value({'key': 'value'}) == '[complex value]'
    assert format_value('string') == 'string'
    assert format_value(42) == 42