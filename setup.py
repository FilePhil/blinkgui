from distutils.core import setup
setup(name='blink',
      version='0.1',
      author='Christoph Hirtz',
      author_email='christoph.hirtz@online.de',
      maintainer='Christoph Hirtz',
      maintainer_email='christoph.hirtz@online.de',
      description='GUI for blinking LED grids',
      requires=['serial', 'numpy', 'lxml', 'pyside'],
      scripts=['blinkgui'],
      py_modules=['blinkgui', 'avrconnector', 'blinkcomponents', 'blinkconfig', 'bmlparser',
                  'colorgenerator', 'generator_dialogs', 'gridgraphicsview', 'lg_dialog',
                  'color_transition_dialog', 'mainwindow', 'res_rc', 'undocommands'],
      )