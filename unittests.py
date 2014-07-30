import unittest
from kalu_parser import VERSION, HELP
import subprocess
from expected_results_from_unittests import expected_news, expected_aur


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
        subprocess.check_output(["./kalu_parser.py", "aur -f"], input=expected_aur,
                                shell=True, universal_newlines=True)


class TestGetUpdatesInfoFromFile(unittest.TestCase):
    def test_get_update_info(self):
        expected = """poppler 0.26.2-1 -> 0.26.3-1
poppler-glib 0.26.2-1 -> 0.26.3-1
apvlv 0.1.4.20121023-3 -> 0.1.4.20121023-4
xdg-utils 1.1.0.git20140426-1 -> 1.1.0.git20140630-1
libexif none -> 0.6.21-2
libdbus 1.8.4-1 -> 1.8.6-1
dbus 1.8.4-1 -> 1.8.6-1
libsystemd 214-2 -> 215-4
systemd 214-2 -> 215-4
harfbuzz 0.9.29-1 -> 0.9.32-1
chromium 35.0.1916.153-1 -> 36.0.1985.125-1
cryptsetup 1.6.4-1 -> 1.6.5-1
dhcpcd 6.4.0-1 -> 6.4.2-1
diffutils 3.3-1 -> 3.3-2
elfutils 0.158-3 -> 0.159-1
v4l-utils 1.0.1-1 -> 1.2.1-1
x265 1.1-1 -> 1.2-1
ffmpeg 1:2.2.4-2 -> 1:2.2.4-3
filesystem 2014.06-2 -> 2014.07-1
git 2.0.1-1 -> 2.0.2-1
vim-runtime 7.4.335-4 -> 7.4.373-1
gvim 7.4.335-4 -> 7.4.373-1
lib32-elfutils 0.158-2 -> 0.159-1
lib32-expat 2.1.0-1 -> 2.1.0-2
lib32-harfbuzz 0.9.29-1 -> 0.9.30-1
lib32-libdbus 1.8.4-1 -> 1.8.6-1
lib32-libsamplerate 0.1.8-1 -> 0.1.8-2
lib32-libxdmcp 1.1.1-1 -> 1.1.1-2
libxcb 1.10-2 -> 1.10-3
lib32-libxcb 1.10-2 -> 1.10-3
lib32-libxdamage 1.1.4-1 -> 1.1.4-2
libxi 1.7.2-1 -> 1.7.4-1
lib32-libxi 1.7.2-1 -> 1.7.3-1
lib32-libxss 1.2.2-1 -> 1.2.2-2
lib32-systemd 214-1 -> 215-1
mesa 10.2.3-1 -> 10.2.4-1
lib32-mesa 10.2.3-1 -> 10.2.4-1
lib32-nvidia-304xx-utils 304.121-3 -> 304.123-1
lib32-nvidia-304xx-libgl 304.121-3 -> 304.123-1
lib32-v4l-utils 1.0.1-1 -> 1.2.1-1
libcups 1.7.3-4 -> 1.7.4-1
libmariadbclient 5.5.37-1 -> 10.0.12-1
libsodium 0.6.0-1 -> 0.6.1-1
linux 3.15.4-1 -> 3.15.5-2
man-pages 3.69-1 -> 3.70-1
mariadb-clients 5.5.37-1 -> 10.0.12-1
mariadb 5.5.37-1 -> 10.0.12-1
nvidia-304xx-utils 304.121-3 -> 304.123-1
nvidia-304xx-libgl 304.121-3 -> 304.123-1
nvidia-304xx 304.121-6 -> 304.123-1
patch 2.7.1-2 -> 2.7.1-3
python2-pillow 2.5.0-1 -> 2.5.1-1
s-nail 14.7.1-1 -> 14.7.4-1
spl-utils-git 0.6.3_r0_g31cb538_3.15.4_1-1 -> 0.6.3_r0_g31cb538_3.15.5_2-2
spl-git 0.6.3_r0_g31cb538_3.15.4_1-1 -> 0.6.3_r0_g31cb538_3.15.5_2-2
svga-dri 10.2.3-1 -> 10.2.4-1
systemd-sysvcompat 214-2 -> 215-4
which 2.20-6 -> 2.20-7
xterm 308-1 -> 309-1
zfs-utils-git 0.6.3_r0_g07dabd2_3.15.4_1-1 -> 0.6.3_r0_g07dabd2_3.15.5_2-2
zfs-git 0.6.3_r0_g07dabd2_3.15.4_1-1 -> 0.6.3_r0_g07dabd2_3.15.5_2-2"""
        subprocess.check_output(["./kalu_parser.py", "updates -f"], input=expected,
                                shell=True, universal_newlines=True)


if __name__ == '__main__':
    unittest.main()
