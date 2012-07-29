from setuptools import setup, find_packages
from setuptools import Command


class Doc(Command):
    """Command to generate documentation"""
    """ TODO:
        * add --sphinxopts command to replace SHINXOPTS
        * add --sphinxbuild command to set sphinxbuild command
        * add --builddir command to set build directory
        * rewrite process_images.sh in python
    """

    description = "Generate documentation"

    user_options = [
        ('formats=', None,
         'formats for documentation (comma-separated list)')]

    def initialize_options(self):
        self.formats = None

    def finalize_options(self):
        if self.formats is None:
            self.formats = ['html']
        else:
            self.formats = [
                format.strip() for format in self.formats.split(',')]

    def run(self):
        import os
        import sphinx
        from subprocess import call

        sphinxbuild = os.environ.get('SPHINXBUILD', 'sphinx-build')
        args = '{0} -b {1} -d ./build/doctere -W ./doc/source build'

        for fmt in self.formats:
            call(['./doc/process_images.sh'])
            sphinx.main(args.format(sphinxbuild, fmt).split())

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
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['*test*']),
    install_requires=['SQLAlchemy>=0.7.6'],
    test_suite='tests',
    cmdclass={
        'doc': Doc
    },
)
