try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = [
    'docopt',
    'schema',
]

tests_require = [
    'six',
]

setup(
    name='pydiceware',
    description='Generate passphrases using the Diceware algorithm.',
    long_description=open('README.rst').read(),
    author='Tom Offermann',
    url='http://github.com/toffer/pydiceware',
    author_email='tom@offermann.us',
    version='0.1.0',
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
    },
    packages=['diceware'],
    package_data={'diceware': ['data/beale.wordlist.asc',
                               'data/diceware.wordlist.asc',
                               'data/metadata.json']
                 },
    entry_points={
        'console_scripts':
            ['diceware-passphrase = diceware.main:main',]
    }
)
