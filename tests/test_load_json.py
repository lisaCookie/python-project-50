import json
from unittest.mock import mock_open, patch

import pytest

from gendiff.load_json import load_json


def test_load_json_success():
    mock_data = {'key1': 'value1', 'key2': 'value2'}
    mock_file = mock_open(read_data=json.dumps(mock_data))

    with patch('builtins.open', mock_file):
        result = load_json('fake_path.json')
        assert result == mock_data


def test_load_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_json('non_existent_file.json')
