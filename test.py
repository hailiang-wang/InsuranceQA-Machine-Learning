#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <> All Rights Reserved
#
#
# File: /Users/hain/ai/InsuranceQA-Machine-Learning/test
# Author: Hai Liang Wang
# Date: 2017-08-08:21:27:06
#
#===============================================================================

"""
   
"""
from __future__ import print_function
from __future__ import division

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-08-08:21:27:06"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")
    # raise "Must be using Python 3"

import unittest

# run testcase: python /Users/hain/ai/InsuranceQA-Machine-Learning/test Test.testExample
class Test(unittest.TestCase):
    '''
    
    '''
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExample(self):
        print("foo")

def test():
    unittest.main()

# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
    
