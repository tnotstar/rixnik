# -*- coding: utf-8 -*-
#
# Copyright 2012-2013 Antonio Alvarado Hernández
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
"""
This script implements a test suite for the module `rixnik.data.portfolio`.
"""

from rixnik.data.portfolio import *

import unittest


class TestPortfolio(unittest.TestCase):
    """Tests for the `Portfolio` class."""

    def test_ctor_argcount(self):
        """No default constructor."""
        self.assertRaises(TypeError, Portfolio)

    def test_ctor_argtype(self):
        """Bad assets type."""
        self.assertRaises(TypeError, Portfolio, None)

    def test_ctor_minassets(self):
        """Minimal number of assets."""
        self.assertRaises(ValueError, Portfolio, [])

        Portfolio(['AAPL'])
        Portfolio(['AAPL GOOG'])

    def test_ctor_assetstr(self):
        """Assets could come as a string."""
        self.assertRaises(ValueError, Portfolio, "")

        Portfolio("AAPL")
        Portfolio("AAPL GOOG")
        Portfolio("AAPL GOOG IBM MSFT ORCL")

    def test_ctor_weighted(self):
        """Weights could be passed."""
        assets = "AAPL GOOG IBM MSFT ORCL".split()
        weights = [.1, .2, .3, .2, .2]
        Portfolio(assets, weights)


if __name__ == '__main__':
    unittest.main()

# EOF
