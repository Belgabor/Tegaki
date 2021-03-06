# -*- coding: utf-8 -*-

from distutils.core import setup
import os

def _getversion(path):
    currdir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(currdir, path)
    import re
    regexp = re.compile(r"VERSION = '([^']*)'")
    f = open(path)
    buf = f.read()
    f.close()
    return regexp.search(buf).group(1)

def getversion():
    convert = _getversion('src/tegaki-convert')
    eval_ = _getversion('src/tegaki-eval')
    build = _getversion('src/tegaki-build')
    return max(convert, eval_, build)

# Please run
# python setup.py install   

setup(
    name = 'tegaki-tools',
    description = 'A set of command-line tools for Tegaki.',
    author = 'Mathieu Blondel',
    author_email = 'mathieu ÂT mblondel DÔT org',
    url = 'http://www.tegaki.org',
    version = getversion(),
    license='GPL',
    scripts = ['src/tegaki-convert', 'src/tegaki-build', 'src/tegaki-eval'],
    packages = ['tegakitools'],
    package_dir = {'tegakitools':'src/tegakitools'}
)