#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

import unittest

def main():
    unittest.main()

if __name__ == '__main__':
    main()
