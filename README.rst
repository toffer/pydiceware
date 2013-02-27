PyDiceware
===========

*Create easy-to-remember, hard-to-guess passphrases using the Diceware algorithm.*

What is Diceware?
-----------------
Invented by Arnold Reinhold in 1995, and extensively described on his `Web site`_, Diceware is a method of creating random passphrases using dice and a specially crafted list of 7776 words. Generating a passphrase is as simple as randomly selecting several words from the word list and joining them together.

.. _Web site: http://world.std.com/~reinhold/diceware.html

But, how do you ensure that you are selecting words at random? Reinhold's answer was to use dice. To select one word from the list, you roll five dice, take the result as a 5-digit number (16512), and look up the word that corresponds to that number ('chisel'). To create a passphrase, you repeat the process and look up multiple words.

This explains why a Diceware word list is exactly 7776 words long. Since there are 6**5, or 7776, possible outcomes when you roll five dice, a Diceware word list must contain just that many words, so that each possible dice roll maps to a single, unique word.

Of course, all that dice-rolling and word-looking-up can be a bit tiresome when you use the Diceware method, so PyDiceware automates the work. It chooses passwords and creates passphrases using the exact same Diceware algorithm, except that it lets the computer roll the dice for you.


But, isn't using a computer to roll dice a bad idea?
----------------------------------------------------
Well, yes...it may be. Good point. As Reinhold says in the `Diceware FAQ`_:

.. _Diceware FAQ: http://world.std.com/~reinhold/dicewarefaq.html#computer

  "Generating truly random numbers using a computer is very tricky. The so-called random number generators that come with most programming libraries are nowhere near good enough. For most users dice is by far a better way to select passphrase words."

In other words, if you generate random numbers with the random.Random class from the Python standard library, then you are using a pseudo-random number generator, and that may not be quite up to snuff.

Luckily, there exist other options for random number generation.


Alternate random number generators (RNGs)
-----------------------------------------
* ``random.SystemRandom``

  Class that uses the os.urandom() function for generating random numbers from sources provided by the operating system. 

* ``randomSources.QuantumRandom``

  The Australian National University has a `Quantum Random Numbers Server`_ with an API. Random numbers are generated "by measuring the quantum fluctuations of a vacuum."

  .. _Quantum Random Numbers Server: http://qrng.anu.edu.au/

* ``randomSources.RandomDotOrg``

  `Random.org`_ hosts a true random number generator service that deploys radios to listen to atmospheric noise, which it uses as its source of randomness.

  .. _Random.org: http://www.random.org/

Personally, I like all of my random numbers to be imported from Australia, but, if you prefer otherwise, PyDiceware makes it simple to swap in the random number generator of your choice.


Installation
============
This package hasn't been uploaded to PyPI yet, so for now, it must be installed manually:

.. code-block:: bash

    $ python setup.py install

In order to run the included ``diceware-passphrase.py`` script, the following dependencies will also be installed:

* RandomSources
* docopt
* schema


Usage
=====

PyDiceware comes with a command line script: ``diceware-passphrase.py``.

Generate a passphrase of 5 words (default):

.. code-block:: bash

    $ diceware-passphrase.py
    croft 10th edwin hulk ee

Generate a passphrase of 7 words, using the 'beale' word list:

.. code-block:: bash

    $ diceware-passphrase.py --words 7 --source beale
     kids queen one loses ty mosaic adler

Get help:

.. code-block:: bash

    $ diceware-passphrase.py --help
    Usage:
      diceware-passphrase.py [--words=<num> --source=<src>]

    Options:
      -h, --help           Show help.
      -w, --words=<num>    Number of words in passphrase [default: 5]
      -s, --source=<src>   Word list to use as password source.
                           [default: diceware]

If the command-line script doesn't provide enough flexibility, you can also use PyDiceware as a library.

Create Diceware object and get passphrase:

.. code-block:: python

    >>> import diceware
    >>> import random

    >>> rng = random.SystemRandom()
    >>> dw = diceware.Diceware(rng=rng)
    >>> dw.passphrase()
    'wispy gar dakar ss sixty'

Use an alternate random number generator and an alternate data source (included with the PyDiceware package):

.. code-block:: python

    >>> import randomSources

    >>> rng = randomSources.RandomDotOrg()
    >>> dw = diceware.Diceware(rng=rng, data_source='beale')
    >>> dw.passphrase()
    'statue fuzzy mgmt sniff coif'

Supply your own Diceware-formatted word list:

.. code-block:: python

    >>> fh = open('pig_latin_diceware_wordlist.txt', 'r')
    >>> wl = diceware.Wordlist(words=fh, with_keys=True)
    >>> fh.close()
    >>> dw = diceware.Diceware(rng=rng, wordlist=wl)
    >>> dw.passphrase()
    'otslay othbay ineshay inalfay imssway'

Create your own word list and ensure that it is a valid Diceware list:

.. code-block:: python

    >>> all_words = [w.strip() for w in open('/usr/share/dict/words', 'r') if len(w) == 6]
    >>> wl = diceware.Wordlist(words=all_words, with_keys=False)
    >>> wl.is_valid()
    False
    >>> words = all_words[:7776]
    >>> wl = diceware.Wordlist(words=words, with_keys=False)
    >>> wl.is_valid()
    True
    >>> print wl.dumps()[:48]
    11111 aalii
    11112 Aaron
    11113 abaca
    11114 aback


Credits
=======
* `Arnold Reinhold`_, who created the `Diceware method`_. "Diceware" is a trademark of Arnold Reinhold.

.. _Arnold Reinhold: http://world.std.com/~reinhold/
.. _Diceware method: http://world.std.com/~reinhold/diceware.html


License
=======
The following data files are redistributed under the `Creative Commons CC-BY 3.0 license`_.

* ``diceware.wordlist.asc``, created by Arnold Reinhold.
* ``beale.wordlist.asc``, created by Alan Beale.

.. _Creative Commons CC-BY 3.0 license: http://creativecommons.org/licenses/by/3.0/

Code is licensed under the MIT license. Copyright (c) 2013 Tom Offermann.
