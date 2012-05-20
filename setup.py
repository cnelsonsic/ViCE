from setuptools import setup, find_packages
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
    test_suite="tests"
)
