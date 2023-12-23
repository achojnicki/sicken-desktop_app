from setuptools import setup

APP = ['Sicken.py']
DATA_FILES = ['views/chat.view']
OPTIONS = {
    'iconfile': 'assets/icons/icon.icns' 
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)