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
        elif print_version.params.parse_options:
            if print_version.params.parse_options == "news":
                with open(print_version.params.file, "r") as file_to_read:
                    count = int(file_to_read.readline()[0])
                    lines = [n for n in file_to_read.readlines() if re.search(r"^- .*", n)]
                    lines = lines[:count]
                    for line in lines:
                        print(line, end="")
            elif print_version.params.parse_options == "aur":
                with open(print_version.params.file, "r") as file_to_read:
                    content = file_to_read.read()
                    count = int(re.search(r"^AUR: .+", content,
                                          re.MULTILINE).group()[5])
                    aur = content.split("AUR: ")[1].replace("- ", "").split("\n")[1:]
                    for line in aur:
                        line = line[3:-4]
                        line = line.replace("</b>", "")
                        line = line.replace("<b>", "")
                        print(line)
            elif print_version.params.parse_options == "updates":
                with open(print_version.params.file, "r") as file_to_read:
                    content = re.search(r"^\d+ updates available.+",
                                        file_to_read.read(),
                                        re.DOTALL | re.MULTILINE).group()
                    content = content.split("AUR")[0].split("\n")[1:-1]
                    for line in content:
                        line = re.search(r"<b>(\w.+)</b>", line).group()
                        line = re.findall(r"<b>(?P<package>[^<]*)</b>\ (?P<old>[^ >]*)\ >\ <b>(?P<new>[^<]*)</b>",
                                         line)
                        updates = " ".join([line[0][0], line[0][1], "->",
                                            line[0][2]])
                        print(updates)
        else:
            with open(print_version.params.file, 'r') as file_to_read:
                for line in file_to_read.readlines():
                    print(line, end="")
    else:
        print(HELP)


print_version.add_param("-H", "--Help", default=True, action="store_true")
print_version.add_param("-v", "--version", help="show version",
                        default=False, action="store_true")
print_version.add_param("-f", "--file", help="read/print file",
                        metavar="FILENAME", nargs="?")
print_version.add_param("parse_options", help="show parse_options", type=str,
                        choices=["news", "aur", "updates"])


if __name__ == "__main__":
    print_version.run()
