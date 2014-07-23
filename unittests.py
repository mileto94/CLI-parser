import unittest
import kalu_parser


class TestGetVersion(unittest.TestCase):
    def test_get_right_version(self):
        print(kalu_parser.VERSION)
        self.assertEqual(kalu_parser.VERSION, kalu_parser.print_version())

    def test_get_wrong_version(self):
        self.assertEqual("000", kalu_parser.print_version())


if __name__ == '__main__':
    unittest.main()
