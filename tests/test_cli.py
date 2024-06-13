import pytest
from log_analyzer.cli import parse_arguments


@pytest.fixture
def set_sys_argv(monkeypatch):
    def _patch_argv(new_argv):
        monkeypatch.setattr('sys.argv', new_argv)
    return _patch_argv


def test_single_input_file(set_sys_argv):
    set_sys_argv([
        'script_name.py', 'input.log', 'output.json'])

    args = parse_arguments()

    assert args.input == ['input.log']
    assert args.output == 'output.json'
    assert args.mfip is False
    assert args.lfip is False
    assert args.eps is False
    assert args.bytes is False


def test_multiple_input_files(set_sys_argv):
    set_sys_argv(
        ['script_name.py', 'input1.log',
         'input2.log', 'input3.log', 'output.json'])

    args = parse_arguments()

    assert args.input == ['input1.log', 'input2.log', 'input3.log']
    assert args.output == 'output.json'
    assert args.mfip is False
    assert args.lfip is False
    assert args.eps is False
    assert args.bytes is False


def test_combination_of_flags(set_sys_argv):
    set_sys_argv(
        ['script_name.py', 'input.log', 'output.json', '--mfip', '--eps'])

    args = parse_arguments()

    assert args.input == ['input.log']
    assert args.output == 'output.json'
    assert args.mfip is True
    assert args.lfip is False
    assert args.eps is True
    assert args.bytes is False
