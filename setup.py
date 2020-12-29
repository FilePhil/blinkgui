#!/usr/bin/env python3
import sys
from blinkconfig import VERSION, AUTHOR, MAIL

base = None
if sys.platform == "win32":
    from cx_Freeze import setup, Executable
    base = "Win32GUI"
else:
    from distutils.core import setup

setup(name='blink',
    version=VERSION,
    author=AUTHOR,
    author_email=MAIL,
    maintainer=AUTHOR,
    maintainer_email=MAIL,
    description='GUI for blinking LED grids',
    requires=['serial', 'numpy', 'lxml', 'PySide2', 'pil'],
    scripts=['blinkgui', 'blinkclient.py', 'blinkserver.py', 'ethernet_server.py', 'simple_player.py'],
    #executables = [Executable("blinkgui.py", base=base)],
    data_files=[("share/blink", ["blink_icon.xpm"]),
        ("share/applications", ["blink.desktop"]),
        ("share/doc/blink", ["blinkrc.example"])],
    classifiers=["Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: German",
        "Natural Language :: English",
        "Topic :: Multimedia :: Graphics :: Editors",
        "Topic :: Multimedia :: Graphics :: Editors :: Raster-Based",
        "Topic :: Multimedia :: Graphics :: Viewers",
        "Topic :: Multimedia :: Video :: Display",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Utilities"],
    py_modules=['blinkgui', 'avrconnector', 'blinkcomponents', 'blinkconfig', 'bmlparser',
                    'colorgenerator', 'gridgraphicsview', 'lg_dialog',
                    'color_transition_dialog', 'mainwindow', 'res_rc', 'undocommands', 'text_dialog',
                    'blinkclient', 'blinkserver', 'ethernet_server', 'simple_player', 'socket_protocol',
                    'simple_dialogs', 'ethernet_dialog'],
    )