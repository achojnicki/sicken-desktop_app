import sys

sys.setrecursionlimit(1000000)
from setuptools import setup

APP = ['Sicken.py']
DATA_FILES = ['views/chat.view']
OPTIONS = {
    'iconfile': 'assets/icons/icon.icns',
    'includes': ['wx','sys','html','requests','socketio'],
    'excludes': ['numpy','scipy','transformers','torch','gevent','matplotlib','pil','jinja2','werkzeug','flask','jedi','markupsafe','test']
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={
        'py2app': OPTIONS,
        },
    setup_requires=['py2app'],
)