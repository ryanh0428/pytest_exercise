"""
This module contains a basic accumulator class.
Its purpose is to show how to use the pytest framework for testing class
"""

# ------------------------------------
# Class: Accumulator
# ------------------------------------


class Accumulator:
    def __init__(self):
        self._count = 0

    @property  # with the decorator property, the caller can get the property but cannot set the value directly with the assignment statment
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more
