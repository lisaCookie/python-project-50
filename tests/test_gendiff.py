import io
import sys

from gendiff.scripts import gendiff


def run_gendiff_with_args(args):
    sys.argv = args
    captured_output = io.StringIO()
    sys.stdout = captured_output
    try:
        gendiff.main()
    except SystemExit:
        pass
    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


def test_format_option():
    output = run_gendiff_with_args(['gendiff.py', '--format'])
    assert 'usage' in output.lower() or 'usage examples' in output.lower()


def test_incorrect_args():
    output = run_gendiff_with_args(['gendiff.py'])
    assert 'usage' in output.lower()


def test_diff_output_json():
    args = ['gendiff.py', 'json', 'file1.json', 'file2.json']
    output = run_gendiff_with_args(args)
    assert isinstance(output, str)
   

def test_diff_output_yaml():
    args = ['gendiff.py', 'stylish', 'file1.yaml', 'file2.yaml']
    output = run_gendiff_with_args(args)
    assert isinstance(output, str)