#!/usr/bin/env python
import cli.app
import os


VERSION = __file__ + " 0.0001"
PATH = os.getcwd()


@cli.app.CommandLineApp
def print_version(app):
    if print_version.params.version:
        print(VERSION)


print_version.add_param("-V", "--version", help="show version",
                        default=False, action="store_true")


if __name__ == "__main__":
    print_version.run()
