#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

import unittest

from pagadorvoid import PagadorVoidRequest
from pagadorvoid import PagadorVoidResponse

class PagadorVoidRequestTests(unittest.TestCase):
    pass 
    
class PagadorVoidResponseTests(unittest.TestCase):
    pass

def main():
    unittest.main()

if __name__ == '__main__':
    main()
