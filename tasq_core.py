from rich import print as rprint
from rich.console import Console


class TasqCore:
    def __init__(self):
        self.console = Console()

    def dispatch(self, args:dict):
        rprint(args)