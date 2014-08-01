expected_news = """- MariaDB 10.1 enters [extra]
- MariaDB 10.2 enters [extra]
- MariaDB 10.3 enters [extra]
- MariaDB 10.4 enters [extra]
- MariaDB 10.5 enters [extra]
"""

expected_aur = """xpra-winswitch 0.13.6-1 > 0.13.7-1
xpra-winswitch 0.13.6-2 > 0.13.7-2
xpra-winswitch 0.13.6-3 > 0.13.7-3
"""

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
zfs-git 0.6.3_r0_g07dabd2_3.15.4_1-1 -> 0.6.3_r0_g07dabd2_3.15.5_2-2
"""

expected_updates_brief = """poppler
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
"""

expected_aur_brief = """xpra-winswitch
xpra-winswitch
xpra-winswitch
"""

expected_verbosed_updates = """poppler 0.26.2-1 -> 0.26.3-1 Download  973.04 KiB;  Net Install  0 B
poppler-glib 0.26.2-1 -> 0.26.3-1 Download  202.96 KiB;  Net Install  0 B
apvlv 0.1.4.20121023-3 -> 0.1.4.20121023-4 Download  223.12 KiB;  Net Install  29.00 KiB
xdg-utils 1.1.0.git20140426-1 -> 1.1.0.git20140630-1 Download  50.98 KiB;  Net Install  0 B
libexif none -> 0.6.21-2 Download  331.15 KiB;  Net Install  2.04 MiB
libdbus 1.8.4-1 -> 1.8.6-1 Download  132.96 KiB;  Net Install  0 B
dbus 1.8.4-1 -> 1.8.6-1 Download  399.00 KiB;  Net Install  0 B
libsystemd 214-2 -> 215-4 Download  111.91 KiB;  Net Install  -64.00 KiB
systemd 214-2 -> 215-4 Download  3.56 MiB;  Net Install  30.00 KiB
harfbuzz 0.9.29-1 -> 0.9.32-1 Download  232.40 KiB;  Net Install  73.00 KiB
chromium 35.0.1916.153-1 -> 36.0.1985.125-1 Download  35.96 MiB;  Net Install  890.00 KiB
cryptsetup 1.6.4-1 -> 1.6.5-1 Download  197.72 KiB;  Net Install  13.00 KiB
dhcpcd 6.4.0-1 -> 6.4.2-1 Download  128.43 KiB;  Net Install  -63.00 KiB
diffutils 3.3-1 -> 3.3-2 Download  176.54 KiB;  Net Install  -34.00 KiB
elfutils 0.158-3 -> 0.159-1 Download  666.06 KiB;  Net Install  29.00 KiB
v4l-utils 1.0.1-1 -> 1.2.1-1 Download  506.11 KiB;  Net Install  548.00 KiB
x265 1.1-1 -> 1.2-1 Download  540.92 KiB;  Net Install  -2048 B
ffmpeg 1:2.2.4-2 -> 1:2.2.4-3 Download  5.50 MiB;  Net Install  0 B
filesystem 2014.06-2 -> 2014.07-1 Download  8.79 KiB;  Net Install  0 B
git 2.0.1-1 -> 2.0.2-1 Download  3.87 MiB;  Net Install  9.00 KiB
vim-runtime 7.4.335-4 -> 7.4.373-1 Download  4.77 MiB;  Net Install  103.00 KiB
gvim 7.4.335-4 -> 7.4.373-1 Download  1244.38 KiB;  Net Install  4.00 KiB
lib32-elfutils 0.158-2 -> 0.159-1 Download  231.82 KiB;  Net Install  44.00 KiB
lib32-expat 2.1.0-1 -> 2.1.0-2 Download  52.89 KiB;  Net Install  -218.00 KiB
lib32-harfbuzz 0.9.29-1 -> 0.9.30-1 Download  129.01 KiB;  Net Install  4.00 KiB
lib32-libdbus 1.8.4-1 -> 1.8.6-1 Download  118.85 KiB;  Net Install  0 B
lib32-libsamplerate 0.1.8-1 -> 0.1.8-2 Download  913.18 KiB;  Net Install  -1466.00 KiB
lib32-libxdmcp 1.1.1-1 -> 1.1.1-2 Download  8.59 KiB;  Net Install  -18.00 KiB
libxcb 1.10-2 -> 1.10-3 Download  1001.59 KiB;  Net Install  44.00 KiB
lib32-libxcb 1.10-2 -> 1.10-3 Download  156.88 KiB;  Net Install  45.00 KiB
lib32-libxdamage 1.1.4-1 -> 1.1.4-2 Download  4.52 KiB;  Net Install  -18.00 KiB
libxi 1.7.2-1 -> 1.7.4-1 Download  143.47 KiB;  Net Install  5.00 KiB
lib32-libxi 1.7.2-1 -> 1.7.3-1 Download  26.83 KiB;  Net Install  9.00 KiB
lib32-libxss 1.2.2-1 -> 1.2.2-2 Download  5.21 KiB;  Net Install  -26.00 KiB
lib32-systemd 214-1 -> 215-1 Download  142.03 KiB;  Net Install  -56.00 KiB
mesa 10.2.3-1 -> 10.2.4-1 Download  2.20 MiB;  Net Install  0 B
lib32-mesa 10.2.3-1 -> 10.2.4-1 Download  2.08 MiB;  Net Install  0 B
lib32-nvidia-304xx-utils 304.121-3 -> 304.123-1 Download  10.19 MiB;  Net Install  0 B
lib32-nvidia-304xx-libgl 304.121-3 -> 304.123-1 Download  1352 B;  Net Install  0 B
lib32-v4l-utils 1.0.1-1 -> 1.2.1-1 Download  100.68 KiB;  Net Install  9.00 KiB
libcups 1.7.3-4 -> 1.7.4-1 Download  280.34 KiB;  Net Install  43.00 KiB
libmariadbclient 5.5.37-1 -> 10.0.12-1 Download  4.16 MiB;  Net Install  -24.48 MiB
libsodium 0.6.0-1 -> 0.6.1-1 Download  145.43 KiB;  Net Install  1024 B
linux 3.15.4-1 -> 3.15.5-2 Download  54.32 MiB;  Net Install  2048 B
man-pages 3.69-1 -> 3.70-1 Download  5.18 MiB;  Net Install  6.00 KiB
mariadb-clients 5.5.37-1 -> 10.0.12-1 Download  930.49 KiB;  Net Install  2.77 MiB
mariadb 5.5.37-1 -> 10.0.12-1 Download  10.97 MiB;  Net Install  9.51 MiB
nvidia-304xx-utils 304.121-3 -> 304.123-1 Download  13.23 MiB;  Net Install  422.00 KiB
nvidia-304xx-libgl 304.121-3 -> 304.123-1 Download  1516 B;  Net Install  0 B
nvidia-304xx 304.121-6 -> 304.123-1 Download  4.36 MiB;  Net Install  27.00 KiB
patch 2.7.1-2 -> 2.7.1-3 Download  74.03 KiB;  Net Install  -1024 B
python2-pillow 2.5.0-1 -> 2.5.1-1 Download  459.12 KiB;  Net Install  0 B
s-nail 14.7.1-1 -> 14.7.4-1 Download  246.48 KiB;  Net Install  68.00 KiB
spl-utils-git 0.6.3_r0_g31cb538_3.15.4_1-1 -> 0.6.3_r0_g31cb538_3.15.5_2-2 Download  11.24 KiB;  Net Install  0 B
spl-git 0.6.3_r0_g31cb538_3.15.4_1-1 -> 0.6.3_r0_g31cb538_3.15.5_2-2 Download  160.36 KiB;  Net Install  0 B
svga-dri 10.2.3-1 -> 10.2.4-1 Download  1407.21 KiB;  Net Install  0 B
systemd-sysvcompat 214-2 -> 215-4 Download  5.69 KiB;  Net Install  0 B
which 2.20-6 -> 2.20-7 Download  14.47 KiB;  Net Install  -33.00 KiB
xterm 308-1 -> 309-1 Download  272.11 KiB;  Net Install  0 B
zfs-utils-git 0.6.3_r0_g07dabd2_3.15.4_1-1 -> 0.6.3_r0_g07dabd2_3.15.5_2-2 Download  970.54 KiB;  Net Install  0 B
zfs-git 0.6.3_r0_g07dabd2_3.15.4_1-1 -> 0.6.3_r0_g07dabd2_3.15.5_2-2 Download  686.09 KiB;  Net Install  0 B
"""
