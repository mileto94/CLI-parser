import unittest
import kalu_parser
from cli import app


class TestGetVersion(unittest.TestCase):
    def test_get_right_version(self):
        self.assertIsNotNone(kalu_parser.print_version(app))


if __name__ == '__main__':
    unittest.main()
