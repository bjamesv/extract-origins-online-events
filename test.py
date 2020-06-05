# Module providing unittest test discovery hook for our Doctest testcases

import unittest
import doctest

import extract
    
def load_tests(loader, tests, ignore):
    """
    Expose Doctest testcases to unitest discovery
    per: https://docs.python.org/3/library/doctest.html#unittest-api
    """
    tests.addTests(doctest.DocTestSuite(extract))
    return tests

