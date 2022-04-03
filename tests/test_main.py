"""Tests for main.py."""

import sys

from aneta_wrapping.src.main import main


def test_main():
    """Tests for main.py."""
    sys.argv = []
    main()
