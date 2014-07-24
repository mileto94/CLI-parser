import unittest
from kalu_parser import VERSION
import subprocess


class TestGetVersion(unittest.TestCase):
    def test_get_right_version(self):
        subprocess.check_output(["./kalu_parser.py", "-v"], input=VERSION,
                                shell=True, universal_newlines=True)

if __name__ == '__main__':
    unittest.main()
