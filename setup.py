try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'pydiceware',
    'description': 'Generate passphrases using the Diceware algorithm.',
    'author': 'Tom Offermann',
    'url': '',
    'download_url': '',
    'author_email': 'tom@offermann.us',
    'version': '0.1',
    'packages': ['diceware'],
    'package_data': {'diceware': ['data/beale.wordlist.asc',
                                  'data/diceware.wordlist.asc',
                                  'data/metadata.json']
                    },
}

setup(**config)
