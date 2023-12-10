import pytest
from tasq import main


class TestCLIArgumentParser:
    @pytest.fixture(autouse=True)
    def setup(self):
        ...

    def test_add(self):
        args = ['add', 'task', 'due:tomorrow']
        main(args)