from setuptools import setup, Command

class UnitTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess

        errno = subprocess.call(
            [sys.executable, '-m', 'unittest', 'discover', '-s', 'tests']
        )

        raise SystemExit(errno)

setup(
    name='ViCE',
    version='0.0.1',
    packages=['vice', 'vice.plugins', 'vice.plugins.rules'],
    cmdclass = {'test': UnitTest}
)
