#!/usr/bin/env python

import diceware
import randomSources

def main():
    rng = randomSources.QuantumRandom()
    dw = diceware.Diceware(rng, data_source='diceware')
    print dw.passphrase()

if __name__ == '__main__':
    main()
