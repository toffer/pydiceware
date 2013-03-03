import random
import sys
import unittest

from six import StringIO

from .context import diceware
from diceware import main

class TestDicewareMain(unittest.TestCase):

    def setUp(self):
        # Save originals, so we can restore in tearDown
        self.orig_stdout = sys.stdout
        self.orig_stderr = sys.stderr

        self.stdout, self.stderr = StringIO(), StringIO()

        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def tearDown(self):
        # Restore originals
        sys.stdout = self.orig_stdout
        sys.stderr = self.orig_stderr

    def test_main(self):
        args = {'--words': '5', '--source':'diceware'}
        main.main(args)
        output = self.stdout.getvalue()
        self.assertEqual(len(output.split()), 5)
