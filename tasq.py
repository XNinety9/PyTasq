from argparser import CLIArgumentParser
from tasq_core import TasqCore


def main(args=None):
    parser = CLIArgumentParser()
    arguments = parser.parse_args(args)
    core = TasqCore()
    core.dispatch(arguments)


if __name__ == "__main__":
    main()
