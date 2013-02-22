import itertools
import re

class Wordlist(object):
    """
    A list of words used in the creation of Diceware passphrases.

    """
    def __init__(self, words=None, with_keys=True):
        self.words = []
        if words:
            self.load(words, with_keys)

    def load(self, words, with_keys):
        """
        Load list of words into self.words.

        load() can handle 2 types of lists:

            Diceware Format (with_keys == True):

                Each input 'word' is a string containing a Diceware key
                and a word, separated by a tab. A Diceware key is a
                string representation of five dice rolls (i.e '12345').

                load() will filter out input words that don't match the
                Diceware format.

            Single Word Format (with_keys == False):

                Each input 'word' is a string.

                No filtering word is done, so all words are accepted.

        """
        if with_keys:
            regex = re.compile('\d{5}\s+(\S+)')
            wl = [m.group(1) for w in words for m in [regex.match(w)] if m]
        else:
            wl = [word.strip() for word in words]
        self.words = wl

    def __len__(self):
        """Return length of wordlist."""
        return len(self.words)

    def _dice_keys(self):
        """
        Create all possible Diceware keys.

        Returns:
            List of Diceware keys in ascending numerical order.

        """
        dice = [tuple('123456') for x in range(5)]
        keys = ["".join(x) for x in itertools.product(*dice)]
        return keys

    def dump(self):
        """Return wordlist as list of (key, word) tuples."""
        return list(zip(self._dice_keys(), self.words))

    def dumps(self):
        """
        Return wordlist as Diceware-formatted, multi-line string.

        Each line of string consists of a Diceware key and a word,
        separated by a tab.

        Returns:
            String of tab-separated key, word pairs, separated by newlines.

        """
        pairs = self.dump()
        wordlist = ["{0}\t{1}".format(k, v) for (k, v) in pairs]
        return "\n".join(wordlist)

    def get(self, index):
        """Lookup word by index."""
        return self.words[index]

    def _validate_uniqueness(self):
        """
        Ensure each word in wordlist is unique.

        Returns:
            True, if all words in list are unique.
            False, if duplicate words exist.

        """
        return len(set(self.words)) == len(self.words)

    def _validate_length(self):
        """
        Ensure wordlist is exactly 7776 words long.

        A valid Diceware list contains one word for each possible
        combination of 5 dice rolls, or 6**5.

        Returns:
            True, if length == 7776.
            False, if length != 7776.

        """
        return len(self.words) == pow(6, 5)

    def is_valid(self):
        """
        Ensure wordlist passes validation tests.

        Returns:
            True, if it passes all validation tests.
            False, if it fails one or more validation tests.

        """
        results = []
        results.append(self._validate_uniqueness())
        results.append(self._validate_length())
        return all(results)
