import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import diceware

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TEST_DATA_FILE = os.path.join(TEST_DATA_DIR, 'short.wordlist.asc')
