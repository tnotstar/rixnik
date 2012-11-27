# -*- coding: utf-8 -*-
#
# Copyright 2012 Antonio Alvarado Hernández
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
"""\
This script implement a test suite for package `rixnik.portfolio`.
"""
print 1
import sys
print sys.path
from rixnik.data.portfolio import *
print 2

import pandas
import unittest


PORTFOLIO_TITLE = "Testing Portfolio"


class TestPortfolio(unittest.TestCase):
    """ A test case for the `rixnik.data.portfolio` objects."""

    def setUp(self):
        pass

    def test_title_ctor(self):
        p = Portfolio(PORTFOLIO_TITLE)
        self.assertEqual(p.title, PORTFOLIO_TITLE)

    def test_title_rdonly(self):
        p = Portfolio(PORTFOLIO_TITLE)
        with self.assertRaises(AttributeError):
            p.title = "Title SHOULD be read-only"


if __name__ == '__main__':
    unittest.main()

# EOF