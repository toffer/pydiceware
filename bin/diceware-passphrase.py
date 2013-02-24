#!/usr/bin/env python

"""
Usage:
  diceware-passphrase.py [--words=<num> --source=<src>]

Options:
  -h, --help           Show help.
  -w, --words=<num>    Number of words in passphrase [default: 5]
  -s, --source=<src>   Word list to use as password source.
                       [default: diceware]

"""
import diceware
import randomSources
import sys

from docopt import docopt, printable_usage
from schema import Schema, SchemaError, And, Use

def main(args):
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
              })

    # Validate args
    try:
        args = s.validate(args)
    except SchemaError as e:
        sys.stderr.write(str(e) + '\n')
        print printable_usage(__doc__)
        return 2

    # And finally...get passphrase!
    rng = randomSources.QuantumRandom()
    dw = diceware.Diceware(rng, data_source=args['--source'])
    print dw.passphrase(num_words=args['--words'])

if __name__ == '__main__':
    args = docopt(__doc__)
    sys.exit(main(args))
