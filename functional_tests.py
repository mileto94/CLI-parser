from cli.test import FunctionalTest
import os
from kalu_parser import PATH, VERSION, HELP
import unittest
import subprocess


class TestKaluParser(FunctionalTest):
    def test_print_version(self):
        command = "kalu_parser.py -V"
        result = self.run_script(os.path.join(PATH, command))
        result.stdout = result.stdout.decode('utf-8')
        result.stderr = result.stderr.decode('utf-8')
        print(result.stdout)
        self.assertScriptDoes(result, stdout=VERSION, trim_output=True)

    def test_print_help(self):
        command = "./kalu_parser.py"
        result = self.run_script(os.path.join(PATH, command))
        result.stdout = result.stdout.decode('utf-8')
        result.stderr = result.stderr.decode('utf-8')
        self.assertScriptDoes(result, stdout=HELP, trim_output=True)

    def test_read_some_file(self):
        with open("./f.txt", "r") as file_to_read:
            expected = file_to_read.read()
        subprocess.check_output(["cat", "f.txt"], shell=True,
                                universal_newlines=True, input=expected)

    def test_move_stdout_in_file(self):
        with open("./d.txt", "r") as file_to_read:
            expected = file_to_read.read()
        subprocess.check_output(["cat", "f.txt"], shell=True,
                                universal_newlines=True, input=expected)

if __name__ == '__main__':
    unittest.main()
