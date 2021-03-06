import json
import pkgutil

from .wordlist import Wordlist


class Diceware(object):
    """
    Generate random passphrases using the Diceware algorithm.

    """
    _js = pkgutil.get_data('diceware', 'data/metadata.json')
    _js = _js.decode('utf-8')
    WORDLISTS_META = json.loads(_js)

    PUNCT_MARKS =  '~!#$%^&*()-=+[]\\{}:;"\'<>?/'

    def __init__(self, rng, data_source='diceware', wordlist=None):
        self.rng = rng
        if wordlist:
            self.wordlist = wordlist
        else:
            # Make wordlist from one of packaged data files.
            meta = Diceware.WORDLISTS_META[data_source]
            data = pkgutil.get_data('diceware', 'data/%s' % meta['filename'])
            data = data.decode('utf-8')
            self.wordlist = Wordlist(data.splitlines())

    def random_char(self):
        i = self.rng.randrange(0, len(self.PUNCT_MARKS))
        return self.PUNCT_MARKS[i]

    def random_num(self):
        return self.rng.randrange(0, 10)

    def insert(self, sub, string, index=None):
        if index is None:
            index = self.rng.randrange(0, len(string) + 1)
        return string[:index] + sub + string[index:]

    def password(self):
        """
        Get password.

        Returns:
            Randomly selected word.

        """
        index = self.rng.randrange(0, len(self.wordlist))
        return self.wordlist.get(index)

    def passphrase(self, num_words=5, add_char=False, add_num=False):
        """
        Get passphrase.

        Returns:
            Randomly generated passphrase, consisting of num_words
            passwords separated by spaces.

        """
        passphrase = " ".join([self.password() for n in range(num_words)])
        if add_char:
            passphrase = self.insert(self.random_char(), passphrase)
        if add_num:
            passphrase = self.insert(str(self.random_num()), passphrase)
        return passphrase

