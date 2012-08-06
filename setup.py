import os
import sys
import shutil
from setuptools import setup, find_packages
from setuptools import Command
from setuptools.command.test import test


class PyTest(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        pytest.main(self.test_args)

class doc(Command):
    """Command to generate documentation"""

    # TODO:
    # * print more useful output after each command
    # * fix pdf output
    # * ghpages format
    # * --github command for use with ghpages format

    description = "Generate documentation"

    user_options = [
        ('formats=', None,
         'formats for documentation (comma-separated list)'),
        ('builddir=', None,
         'directory in which to build documentation'),
        ('sourcedir=', None,
         'directory where documentation source exists'),
        ('sphinxbuild=', None,
         'name of sphinx-build executable'),
        ('sphinxopts=', None,
         'options to pass to sphinx-build'),
        ('clean', None,
         'remove genenerated documenation files')]

    def initialize_options(self):
        self.formats = None
        self.builddir = None
        self.sourcedir = None
        self.sphinxbuild = None
        self.sphinxopts = None
        self.clean = None

    def finalize_options(self):
        if not self.formats:
            self.formats = ['html']
        else:
            self.formats = [
                format.strip() for format in self.formats.split(',')]

        if not self.builddir:
            self.builddir = 'build'

        if not self.sourcedir:
            self.sourcedir = os.path.join('doc', 'source')

        if not self.sphinxbuild:
            self.sphinxbuild = os.path.join(
                os.environ.get('PYTHONPATH', './'), 'sphinx-build')

        if not self.sphinxopts:
            self.sphinxopts = '-W'

        if self.clean is None:
            self.clean = False

    def run(self):
        if self.clean:
            shutil.rmtree(self.builddir)
        else:
            import sphinx

            sphinxbuild = os.environ.get('SPHINXBUILD', self.sphinxbuild)
            sphinxopts = os.environ.get('SPHINXOPTS', self.sphinxopts)
            args = '{0} -b {1} -d {2}/doctree {3} {4} {2}/{1}'

            self._process_images()
            for fmt in self.formats:
                sphinx.main(args.format(sphinxbuild,
                    fmt, self.builddir, sphinxopts, self.sourcedir).split())

    def _process_images(self):
        from subprocess import call

        imagedir = os.path.join(self.sourcedir, '_static')

        # create class and pacakge diagrams
        args = 'pyreverse -my -o svg -p ViCE vice'
        call(args.split())

        for filename in os.listdir('.'):
            if filename.endswith('.svg'):
                try:
                    shutil.move(filename, imagedir)
                except shutil.Error:
                    pass

        # convnert svgs to pngs
        args = 'inkscape -D -e {0} {1}'
        [call(args.format(
            os.path.join(imagedir, filename.replace('svg', 'png')),
            os.path.join(imagedir, filename)).split())
            for filename in os.listdir(imagedir) if filename.endswith('.svg')]


setup(
    name='ViCE',
    version='0.0.1',
    author='Edwin Marshall',
    author_email='aspidites@wtactics.org',
    description=('Portable, open source, modular framework for both creating '
                 'and playing trading card games.'),
    long_description=open('README.rst').read(),
    license='AGPL',
    keywords='tcg ccg python wtactics',
    url='http://aspidites.github.com/ViCE',
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Games/Entertainment :: Turn Based Strategy',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    packages=find_packages(exclude=['*test*']),
    install_requires=['SQLAlchemy>=0.7.6'],
    tests_require=['pytest'],
    cmdclass={
        'doc': doc,
        'test': PyTest})
