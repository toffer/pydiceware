import os
import unittest

from .context import diceware
from .context import TEST_DATA_FILE

class TestWordlistInit(unittest.TestCase):

    def test_diceware_file_input(self):
        with open(TEST_DATA_FILE, 'rb') as fh:
            wl = diceware.Wordlist(fh)
        self.assertEqual(len(wl), 12)

    def test_single_words_input(self):
        data = "aaaa\nzzzz\n".splitlines()
        wl = diceware.Wordlist(data, with_keys=False)
        self.assertEqual(wl.words[0], 'aaaa')


class TestWordlistMethods(unittest.TestCase):

    def setUp(self):
        with open(TEST_DATA_FILE, 'rb') as fh:
            self.wl = diceware.Wordlist(fh)

    def test_dump(self):
        self.assertEqual(self.wl.dump()[0], ('11111', 'a'))
        self.assertEqual(self.wl.dump()[11], ('11126', 'abase'))

    def test_dumps(self):
        start = "11111\ta\n11112\ta&p\n"
        self.assertTrue(self.wl.dumps().startswith(start))

    def test_get_a(self):
        self.assertEqual(self.wl.get(0), 'a')

    def test_get_abase(self):
        self.assertEqual(self.wl.get(11), 'abase')

    def test_index_error(self):
        self.assertRaises(IndexError, self.wl.get, 12)

    def test_is_valid_false(self):
        self.assertFalse(self.wl.is_valid())


if __name__ == '__main__':
    unittest.main()
