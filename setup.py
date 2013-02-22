try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pydiceware',
    description='Generate passphrases using the Diceware algorithm.',
    author='Tom Offermann',
    url='',
    download_url='',
    author_email='tom@offermann.us',
    version='0.1.0',
    install_requires=['randomSources'],
    packages=['diceware'],
    package_data={'diceware': ['data/beale.wordlist.asc',
                               'data/diceware.wordlist.asc',
                               'data/metadata.json']
                 },
    scripts=['bin/diceware-passphrase.py'],
)
