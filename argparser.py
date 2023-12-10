import argparse
from functools import wraps


def command_handler(command_handlers):
    """ Decorator factory for registering command handlers. """

    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            return func(self, *args, **kwargs)

        command_handlers[func.__name__] = wrapper
        return wrapper

    return decorator


class CLIArgumentParser:
    """ Command line interface argument parser. """
    def __init__(self):
        self.command_handlers = {}
        self.register_commands()

        self.parser = argparse.ArgumentParser(description='Process command line arguments.')
        self.parser.add_argument('command', help=f'Command to execute: {self.command_handlers.keys()}')
        self.parser.add_argument('arguments', nargs=argparse.REMAINDER, help='Arguments for the command')

    def parse_args(self, args=None):
        args = self.parser.parse_args(args)
        command = args.command
        if command in self.command_handlers:
            return self.command_handlers[command](self, args.arguments)
        else:
            raise ValueError(f"Command '{command}' is not recognized.")

    def register_commands(self):
        @command_handler(self.command_handlers)
        def add(self, arguments):
            if len(arguments) < 2:
                raise ValueError("Not enough arguments for 'add' command")
            due_date_arg = arguments[-1]
            if not due_date_arg.startswith('due:'):
                raise ValueError("Due date must be in the format 'due:XXX'")
            description = ' '.join(arguments[:-1])
            return {
                'command': 'add',
                'description': description,
                'due_date': due_date_arg
            }

        @command_handler(self.command_handlers)
        def help(self, arguments):
            return {
                'command': 'help'
            }
