#!/usr/bin/env python
import cli.app
import os


VERSION = __file__ + " 0.0001"
PATH = os.getcwd()
HELP = """usage: print_version [-h]\n\noptional arguments:\n-h,
        --help  show this help message and exit"""


@cli.app.CommandLineApp
def print_version(app):
    if print_version.params.version:
        print(VERSION)
    else:
        print(HELP)


print_version.add_param("-H", "--Help", default=True, action="store_true")
print_version.add_param("-v", "--version", help="show version",
                        default=False, action="store_true")


if __name__ == "__main__":
    print_version.run()
