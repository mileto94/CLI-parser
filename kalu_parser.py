#!/usr/bin/env python
import cli.app
import os
import sys
import re


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
        if print_version.params.file == "-":
            for line in sys.stdin.readlines():
                print(line, end="")
        elif print_version.params.news == "news":
            with open(print_version.params.file, "r") as file_to_read:
                lines = [n for n in file_to_read.readlines() if re.search(r"^-\ \w+.*$", n)]
                for line in lines:
                    print(line, end="")
        else:
            with open(print_version.params.file, 'r') as file_to_read:
                for line in file_to_read.readlines():
                    print(line, end="")
    else:
        print(HELP)


print_version.add_param("-H", "--Help", default=True, action="store_true")
print_version.add_param("-V", "--version", help="show version",
                        default=False, action="store_true")
print_version.add_param("-f", "--file", help="read/print file",
                        metavar="FILENAME", nargs="?")
print_version.add_param("news", help="show news", type=str,
                        default="There are no unread news", nargs="?")


if __name__ == "__main__":
    print_version.run()
