#!/usr/bin/env python
import cli.app
import os


VERSION = " ".join([__file__, "version", "0.0001"])
PATH = os.getcwd()
HELP = """usage: ./kalu_parser.py [-h] [-H] [-v] [-f [FILENAME]]

optional arguments:
  -h, --help            show this help message and exit
  -H, --Help
  -v, --version         show version
  -f [FILENAME], --file [FILENAME]
                        read/print file"""


@cli.app.CommandLineApp(name=__file__)
def print_version(app):
    if print_version.params.version:
        print(VERSION)
    elif print_version.params.file:
        with open(print_version.params.file, 'r') as file_to_read:
            for line in file_to_read.readlines():
                print(line, end="")
    else:
        print(HELP)


print_version.add_param("-H", "--Help", default=True, action="store_true")
print_version.add_param("-v", "--version", help="show version",
                        default=False, action="store_true")
print_version.add_param("-f", "--file", help="read/print file",
                        metavar="FILENAME", nargs='?')


if __name__ == "__main__":
    print_version.run()
