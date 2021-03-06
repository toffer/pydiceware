import mock
import random
import unittest

from .context import diceware
from .context import TEST_DATA_FILE


class TestDicewareInit(unittest.TestCase):

    def test_init_diceware(self):
        rng = random.Random()
        dw = diceware.Diceware(rng, data_source='diceware')
        self.assertEqual(dw.wordlist.get(10), 'aback')

    def test_init_beale(self):
        rng = random.Random()
        dw = diceware.Diceware(rng, data_source='beale')
        self.assertEqual(dw.wordlist.get(10), 'abacus')

    def test_init_ignore_data_source_nonnull_wordlist(self):
        rng = random.Random()
        with open(TEST_DATA_FILE, 'r') as fh:
            wl = diceware.Wordlist(fh)
        dw = diceware.Diceware(rng, data_source='diceware', wordlist=wl)
        self.assertEqual(len(dw.wordlist), 12)


class TestDicewareMethods(unittest.TestCase):

    def setUp(self):
        rng = random.Random()
        with open(TEST_DATA_FILE, 'r') as fh:
            wl = diceware.Wordlist(fh)
        self.dw = diceware.Diceware(rng, wordlist=wl)
        self.rand_chars = '~!#$%^&*()-=+[]\\{}:;"\'<>?/'

    def test_rand_char(self):
        self.assertTrue(self.dw.random_char() in self.rand_chars)

    def test_insert(self):
        self.assertTrue('x' in self.dw.insert('x', 'blah'))

    def test_password_first(self):
        self.dw.rng.randrange = mock.Mock(side_effect=[0])
        self.assertEqual(self.dw.password(), 'a')

    def test_password_tenth(self):
        self.dw.rng.randrange = mock.Mock(side_effect=[9])
        self.assertEqual(self.dw.password(), 'ababa')

    def test_passphrase(self):
        expected = "a&p aba abase aaa aaron"
        self.dw.rng.randrange = mock.Mock(side_effect=[1, 8, 11, 4, 6])
        self.assertEqual(self.dw.passphrase(), expected)

    def test_passphrase_with_char(self):
        expected = "a&p aba abase aaa aaro!n"
        self.dw.rng.randrange = mock.Mock(side_effect=[1, 8, 11, 4, 6, 1, 22])
        self.assertEqual(self.dw.passphrase(add_char=True), expected)

    def test_passphrase_with_num(self):
        self.dw.rng.randrange = mock.Mock(side_effect=[10, 4, 4, 8])
        result = self.dw.passphrase(num_words=2, add_num=True)
        expected = "aback aa4a"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
