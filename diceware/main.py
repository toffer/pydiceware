#!/usr/bin/env python

"""
Usage:
  diceware-passphrase.py [--words=<num>] [--source=<src>]
                         [--add-char] [--add-num]

Options:
  -h, --help           Show help.
  -w, --words=<num>    Number of words in passphrase [default: 5]
  -s, --source=<src>   Word list to use as password source.
                       [default: diceware]
  -c, --add-char       Add a random character to passphrase.
  -n, --add-num        Add a random number to passphrase.

"""
from __future__ import print_function

import diceware
import random
import sys

from docopt import docopt, printable_usage
from schema import Schema, SchemaError, And, Use

def main(args=None):
    if args is None:
        args = docopt(__doc__)

    # What word lists are included in diceware package?
    avail_word_lists = diceware.Diceware.WORDLISTS_META.keys()

    # Prep error messages for invalid command line args
    err_words = "--words arg must be a positive integer."
    err_source = "--source arg must be a valid word list."

    # Set up validation schema for command line args
    s = Schema({'--words': And(Use(int),
                               lambda n: n > 0,
                               error=err_words
                              ),
                '--source': And(lambda n: n in avail_word_lists,
                                error=err_source
                               ),
                '--add-char': bool,
                '--add-num': bool,
              })

    # Validate args
    try:
        args = s.validate(args)
    except SchemaError as e:
        sys.stderr.write(str(e) + '\n')
        print(printable_usage(__doc__))
        return 2

    # And finally...get passphrase!
    rng = random.SystemRandom()
    dw = diceware.Diceware(rng, data_source=args['--source'])
    kwargs = {
        'num_words': args['--words'],
        'add_char': args['--add-char'],
        'add_num': args['--add-num'],
    }
    print(dw.passphrase(**kwargs))

if __name__ == '__main__':
    sys.exit(main())
