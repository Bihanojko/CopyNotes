#setup.py
from distutils.core import setup
import py2exe

setup(console=['script.py'],
    options = {
        'py2exe': {
            'packages': ['sys', 're', 'xml.etree.ElementTree', 'io']
        }
    }
)
