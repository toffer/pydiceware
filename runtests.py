#!/usr/bin/env python

import sys
import pytest


def main(args=None):
    """Set args and call pytest.main."""
    if args is None:
        args = []

    if not any(a for a in args[1:] if not a.startswith('-')):
        args.append('tests')

    sys.exit(pytest.main(args))


if __name__ == '__main__':
    main(sys.argv)
