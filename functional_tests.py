from cli.test import FunctionalTest
import os
from kalu_parser import PATH, VERSION
import unittest


class TestKaluParser(FunctionalTest):
    def test_print_version(self):
        command = "kalu_parser.py -v"
        result = self.run_script(os.path.join(PATH, command))
        result.stdout = result.stdout.decode('utf-8')
        result.stderr = result.stderr.decode('utf-8')
        self.assertScriptDoes(result, stdout=VERSION, returncode=0, trim_output=True)


if __name__ == '__main__':
    unittest.main()
