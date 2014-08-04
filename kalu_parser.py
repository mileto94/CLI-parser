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


def exists(filename):
    try:
        file = open(filename, "rb")
        file.close()
        return True
    except IOError:
        print("There is no file with this name!")
        return False


def check_verbosity():
    return kalu_parser.params.verbose


def check_brief():
    return kalu_parser.params.brief


def make_verbosity(line):
    line = re.findall(r"\(D:\s(?P<download>.*)N:\s(?P<net_install>.+)\)",
                      line)
    line = [line[0][0], line[0][1]]
    return line


def print_news():
    with open(kalu_parser.params.file, "r") as file_to_read:
        content = file_to_read.read()
        lines = re.findall(r"^-\ \w+.*$", content, re.MULTILINE)
    for line in lines:
        print(line)
    if check_verbosity() == 2:
        news_size = re.search(r"^\d+", content).group()
        total = ["Total Unread News:", news_size]
        print(" ".join(total))


def print_aur():
    aur = ""
    with open(kalu_parser.params.file, "r") as file_to_read:
        content = file_to_read.read()
        aur = content.split("AUR: ")[1].replace("- ", "")
        aur_number = aur.split(" ")[0]
        aur = aur.split("\n")[1:]
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
            if check_verbosity() == 2:
                total = ["Total Packages Updated:", aur_number]
        else:
            line = " ".join(aur)
        print(line)
    if check_verbosity() == 2:
        print(" ".join(total))


def print_updates():
    total = []
    all_update_info = ""
    content = []
    with open(kalu_parser.params.file, "r") as file_to_read:
        content = re.search(r"^\d+ updates available.+", file_to_read.read(),
                            re.DOTALL | re.MULTILINE).group()
        all_update_info = re.search(r"^\d+ updates.+", content).group()
        content = content.split("AUR")[0].split("\n")[1:-1]
    for line in content:
        newline = re.search(r"<b>(\w.+)</b>", line).group()
        newline = re.findall(r"<b>(?P<package>[^<]*)</b>\ (?P<old>[^ >]*)\ >\ <b>(?P<new>[^<]*)</b>",
                             newline)
        # line is list of tuple[()]:
        if check_brief():
            updates = newline[0][0]
        else:
            updates = [newline[0][0], newline[0][1], "->", newline[0][2]]
            if check_verbosity():
                verbosed = make_verbosity(line)
                updates += ["Download ", verbosed[0], "Net Install ",
                            verbosed[1]]
            updates = " ".join(updates)
            if check_verbosity() == 2:
                number = re.search(r"\d+", all_update_info).group()
                info = make_verbosity(all_update_info)
                d_size = info[0][:-2]
                i_size = info[1]
                total = ["Total Updates Available:", number, "\n",
                         "Download Size:", d_size, "\n",
                         "Net Install Size:", i_size]
        print(updates)
    if check_verbosity() == 2:
        print(" ".join(total))


@cli.app.CommandLineApp(name=__file__)
def kalu_parser(app):
    if kalu_parser.params.version:
        print(VERSION)
    elif kalu_parser.params.file and exists(kalu_parser.params.file):
        if kalu_parser.params.file == "-":
            for line in sys.stdin.readlines():
                print(line, end="")
        elif kalu_parser.params.parse_options:
            if kalu_parser.params.parse_options == "news":
                print_news()
            elif kalu_parser.params.parse_options == "aur":
                print_aur()
            elif kalu_parser.params.parse_options == "updates":
                print_updates()
        elif exists(kalu_parser.params.file):
            with open(kalu_parser.params.file, 'r') as file_to_read:
                for line in file_to_read.readlines():
                    print(line, end="")
    else:
        print(HELP, end="")


kalu_parser.add_param("-H", "--Help", default=True, action="store_true")
kalu_parser.add_param("-V", "--version", help="show version",
                      default=False, action="store_true")
kalu_parser.add_param("-f", "--file", help="read/print file",
                      metavar="FILENAME", nargs="?")
kalu_parser.add_param("parse_options", help="show parse_options", type=str,
                      choices=["news", "aur", "updates"], nargs="?")
kalu_parser.add_param("-b", "--brief", help="show packages without versions",
                      default=0, action="count")
kalu_parser.add_param("-v", "--verbose", help="Show verbose downloading data",
                      default=0, action="count")
kalu_parser.add_param("--vv", "--verbose --verbose", "--verbose=2",
                      help="Show full verbose - with info about all processes done",
                      default=0, action="count")


if __name__ == "__main__":
    kalu_parser.run()
