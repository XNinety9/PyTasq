import pytest
import argparse
from argparser import CLIArgumentParser


class TestCLIArgumentParser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.parser = CLIArgumentParser()

    def test_initialization(self):
        assert isinstance(self.parser.parser, argparse.ArgumentParser)

    def test_command_registration(self):
        assert 'add' in self.parser.command_handlers
        assert 'help' in self.parser.command_handlers

    def test_add_valid_command(self):
        args = ['add', 'task', 'due:tomorrow']
        result = self.parser.parse_args(args)
        assert result == {
            'command': 'add',
            'description': 'task',
            'due_date': 'due:tomorrow'
        }

    def test_help_valid_command(self):
        args = ['help']
        result = self.parser.parse_args(args)
        assert result == {
            'command': 'help'
        }

    def test_parse_args_unrecognized_command(self):
        with pytest.raises(ValueError):
            self.parser.parse_args(['unknown', 'arg1'])

    def test_parse_args_insufficient_arguments(self):
        with pytest.raises(ValueError):
            self.parser.parse_args(['add', 'task'])

    def test_parse_args_incorrect_due_date(self):
        with pytest.raises(ValueError):
            self.parser.parse_args(['add', 'task', 'notaduedate'])

    # You can add more tests for other command handlers and edge cases
