import unittest
from kalu_parser import VERSION, HELP
import subprocess
from expected_results_from_unittests import expected_news


class TestGetVersion(unittest.TestCase):
    def test_get_right_version(self):
        subprocess.check_output(["./kalu_parser.py", "-v"], input=VERSION,
                                shell=True, universal_newlines=True)


class TestHelpMessages(unittest.TestCase):
    def test_get_help_message(self):
        subprocess.check_output(["./kalu_parser.py", "-h"], input=HELP,
                                shell=True, universal_newlines=True)

    def test_get_default_help_message(self):
        subprocess.check_output(["./kalu_parser.py", ""], input=HELP,
                                shell=True, universal_newlines=True)


class TestGetNewsFromFile(unittest.TestCase):
    def test_get_news_from_file(self):
        subprocess.check_output(["./kalu_parser.py", "news -f"],
                                input=expected_news, shell=True,
                                universal_newlines=True)


class TestGetAURInfoFromFile(unittest.TestCase):
    def test_get_aur_info(self):
        expected = """xpra-winswitch 0.13.6-1 > 0.13.7-1
xpra-winswitch 0.13.6-2 > 0.13.7-2
xpra-winswitch 0.13.6-3 > 0.13.7-3"""
        subprocess.check_output(["./kalu_parser.py", "aur -f"], input=expected,
                                shell=True, universal_newlines=True)


if __name__ == '__main__':
    unittest.main()
