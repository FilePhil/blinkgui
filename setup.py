import sys
base = None
if sys.platform == "win32":
    from cx_Freeze import setup, Executable
    base = "Win32GUI"
else:
    from distutils.core import setup

setup(name='blink',
    version='1.0.5',
    author='Christoph Hirtz',
    author_email='christoph.hirtz@online.de',
    maintainer='Christoph Hirtz',
    maintainer_email='christoph.hirtz@online.de',
    description='GUI for blinking LED grids',
    requires=['serial', 'numpy', 'lxml', 'pyside', 'pil'],
    scripts=['blinkgui'],
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
                    'colorgenerator', 'generator_dialogs', 'gridgraphicsview', 'lg_dialog',
                    'color_transition_dialog', 'mainwindow', 'res_rc', 'undocommands', 'text_dialog'],
    )