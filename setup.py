import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='idacute',
    version='1.0.1',
    py_modules=['cute'],
    url='https://github.com/tmr232/Cute',
    license='MIT',
    author='Tamir Bahar',
    author_email='',
    description='Cross-Qt compatibility module for IDAPython',
    long_description=(read('README.rst')),
)
