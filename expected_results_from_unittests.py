expected_news = """
- MariaDB 10.1 enters [extra]
- MariaDB 10.2 enters [extra]
- MariaDB 10.3 enters [extra]
- MariaDB 10.4 enters [extra]
- MariaDB 10.5 enters [extra]"""

expected_aur = """xpra-winswitch 0.13.6-1 > 0.13.7-1
xpra-winswitch 0.13.6-2 > 0.13.7-2
xpra-winswitch 0.13.6-3 > 0.13.7-3"""

expected_updates = """poppler 0.26.2-1 -> 0.26.3-1
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

expected_brief = """poppler
poppler-glib
apvlv
xdg-utils
libexif
libdbus
dbus
libsystemd
systemd
harfbuzz
chromium
cryptsetup
dhcpcd
diffutils
elfutils
v4l-utils
x265
ffmpeg
filesystem
git
vim-runtime
gvim
lib32-elfutils
lib32-expat
lib32-harfbuzz
lib32-libdbus
lib32-libsamplerate
lib32-libxdmcp
libxcb
lib32-libxcb
lib32-libxdamage
libxi
lib32-libxi
lib32-libxss
lib32-systemd
mesa
lib32-mesa
lib32-nvidia-304xx-utils
lib32-nvidia-304xx-libgl
lib32-v4l-utils
libcups
libmariadbclient
libsodium
linux
man-pages
mariadb-clients
mariadb
nvidia-304xx-utils
nvidia-304xx-libgl
nvidia-304xx
patch
python2-pillow
s-nail
spl-utils-git
spl-git
svga-dri
systemd-sysvcompat
which
xterm
zfs-utils-git
zfs-git
xpra-winswitch
xpra-winswitch
xpra-winswitch"""
