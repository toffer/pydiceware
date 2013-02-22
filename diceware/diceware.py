import json
import pkgutil

from .wordlist import Wordlist


class Diceware(object):
    """
    Generate random passphrases using the Diceware algorithm.

    """
    _js = pkgutil.get_data('diceware', 'data/metadata.json')
    WORDLISTS_META = json.loads(_js)

    def __init__(self, rng, data_source='diceware', wordlist=None):
        self.rng = rng
        if wordlist:
            self.wordlist = wordlist
        else:
            # Make wordlist from one of packaged data files.
            meta = Diceware.WORDLISTS_META[data_source]
            data = pkgutil.get_data('diceware', 'data/%s' % meta['filename'])
            self.wordlist = Wordlist(data.splitlines())

    def random_char(self, num_ok=True):
        pass

    def add_char(self, char, passphrase):
        pass

    def password(self):
        """
        Get password.

        Returns:
            Randomly selected word.

        """
        index = self.rng.randrange(0, len(self.wordlist))
        return self.wordlist.get(index)

    def passphrase(self, num_words=5):
        """
        Get passphrase.

        Returns:
            Randomly generated passphrase, consisting of num_words
            passwords separated by spaces.

        """
        return " ".join([self.password() for n in range(num_words)])

