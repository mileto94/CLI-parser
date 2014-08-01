#!/usr/bin/env python
import cli.app
from os.path import basename
import os
import sys
import re


VERSION = " ".join([basename(__file__), "version", "0.0001"])
PATH = os.getcwd()
HELP = """usage: ./kalu_parser.py [-h] [-H] [-v] [-f [FILENAME]]

optional arguments:
  -h, --help            show this help message and exit
  -H, --Help
  -v, --version         show version
  -f [FILENAME], --file [FILENAME]
                        read/print file
"""


def check_verbosity():
    return print_version.params.verbose


def check_brief():
    return print_version.params.brief


def make_verbosity(line):
    line = re.findall(r"\(D:\s(?P<download>.*)N:\s(?P<net_install>.+)\)",
                      line)
    line = [line[0][0], line[0][1]]
    return line


@cli.app.CommandLineApp(name=__file__)
def print_version(app):
    if print_version.params.version:
        print(VERSION)
    elif print_version.params.file:
        if print_version.params.file == "-":
            for line in sys.stdin.readlines():
                print(line, end="")
        elif print_version.params.parse_options:
            if print_version.params.parse_options == "news":
                with open(print_version.params.file, "r") as file_to_read:
                    lines = [n for n in file_to_read.readlines() if re.search(r"^-\ \w+.*$", n)]
                for line in lines:
                    print(line, end="")
            elif print_version.params.parse_options == "aur":
                with open(print_version.params.file, "r") as file_to_read:
                    content = file_to_read.read()
                    aur = content.split("AUR: ")[1].replace("- ", "").split("\n")[1:]
                    for line in aur:
                        newline = re.findall(r"<b>(?P<package>[^<]*)</b>\ (?P<old>[^ >]*)\ >\ <b>(?P<new>[^<]*)</b>",
                                          line)
                        aur = [newline[0][0], newline[0][1], ">", newline[0][2]]
                        if check_brief():
                            line = aur[0]
                        elif check_verbosity():
                            verbosed = make_verbosity(line)
                            v_line = ["Download", verbosed[0], "Net Install", verbosed[1]]
                            line = " ".join(aur + v_line)
                        else:
                            line = " ".join(aur)
                        print(line)
            elif print_version.params.parse_options == "updates":
                with open(print_version.params.file, "r") as file_to_read:
                    content = re.search(r"^\d+ updates available.+",
                                        file_to_read.read(),
                                        re.DOTALL | re.MULTILINE).group()
                    content = content.split("AUR")[0].split("\n")[1:-1]
                    for line in content:
                        newline = re.search(r"<b>(\w.+)</b>", line).group()
                        newline = re.findall(r"<b>(?P<package>[^<]*)</b>\ (?P<old>[^ >]*)\ >\ <b>(?P<new>[^<]*)</b>",
                                             newline)
                        # line is list of tuple[()]:
                        if check_brief():
                            updates = newline[0][0]
                        else:
                            updates = [newline[0][0], newline[0][1], "->",
                                                newline[0][2]]
                            if check_verbosity():
                                verbosed = make_verbosity(line)
                                updates += ["Download ", verbosed[0], "Net Install ",
                                            verbosed[1]]
                            updates = " ".join(updates)
                        print(updates)

        else:
            with open(print_version.params.file, 'r') as file_to_read:
                for line in file_to_read.readlines():
                    print(line, end="")
    else:
        print(HELP, end="")


print_version.add_param("-H", "--Help", default=True, action="store_true")
print_version.add_param("-V", "--version", help="show version",
                        default=False, action="store_true")
print_version.add_param("-f", "--file", help="read/print file",
                        metavar="FILENAME", nargs="?")
print_version.add_param("parse_options", help="show parse_options", type=str,
                        choices=["news", "aur", "updates"], nargs="?")
print_version.add_param("-b", "--brief", help="show packages without versions",
                        default=0, action="count")
print_version.add_param("-v", "--verbose", help="Show verbose downloading data",
                        default=0, action="count")


if __name__ == "__main__":
    print_version.run()
