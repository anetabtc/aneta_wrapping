"""Tests for main.py."""

import os
import shutil
import sys
from typing import Callable

import pytest

from aneta-wrapping.src.main import main

def test_main():
    """Tests for main.py."""
    sys.argv = []
    with pytest.raises(NotImplementedError):
        main()