import unittest
from kalu_parser import VERSION, HELP
import subprocess
from expected_results_from_unittests import expected_news, expected_aur, expected_updates, expected_updates_brief, expected_aur_brief


class TestGetVersion(unittest.TestCase):
    def test_get_right_version(self):
        output = subprocess.check_output("./kalu_parser.py -V", input=VERSION,
                                         shell=True, universal_newlines=True)
        self.assertEqual(output, VERSION + "\n")


class TestHelpMessages(unittest.TestCase):
    def test_get_help_message(self):
        output = subprocess.check_output(["./kalu_parser.py", "-h"], input=HELP,
                                         shell=True, universal_newlines=True)
        self.assertEqual(output, HELP)

    def test_get_default_help_message(self):
        output = subprocess.check_output("./kalu_parser.py", input=HELP,
                                         shell=True, universal_newlines=True)
        self.assertEqual(output, HELP)


class TestGetNewsFromFile(unittest.TestCase):
    def test_get_news_from_file(self):
        output = subprocess.check_output("./kalu_parser.py news -f cli-sample-output.txt",
                                         input=expected_news, shell=True,
                                         universal_newlines=True)
        self.assertEqual(output, expected_news)


class TestGetAURInfoFromFile(unittest.TestCase):
    def test_get_aur_info(self):
        output = subprocess.check_output("./kalu_parser.py aur -f cli-sample-output.txt",
                                         input=expected_aur, shell=True,
                                         universal_newlines=True)
        self.assertEqual(output, expected_aur)


class TestGetUpdatesInfoFromFile(unittest.TestCase):
    def test_get_update_info(self):
        output = subprocess.check_output("./kalu_parser.py updates -f cli-sample-output.txt",
                                         input=expected_updates, shell=True,
                                         universal_newlines=True)
        self.assertEqual(output, expected_updates)


class TestGetBriefPackageView(unittest.TestCase):
    def test_get_updates_brief(self):
        output = subprocess.check_output("./kalu_parser.py updates -b -f cli-sample-output.txt",
                                         input=expected_updates_brief, shell=True,
                                         universal_newlines=True)
        self.assertEqual(output, expected_updates_brief)

    def test_get_aur_brief(self):
        output = subprocess.check_output("./kalu_parser.py aur -b -f cli-sample-output.txt",
                                         input=expected_aur_brief, shell=True,
                                         universal_newlines=True)
        self.assertEqual(output, expected_aur_brief)


if __name__ == '__main__':
    unittest.main()
