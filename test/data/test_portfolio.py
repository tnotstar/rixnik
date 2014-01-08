# -*- coding: utf-8 -*-
#
# Copyright (c) 2012-2014 Antonio Alvarado Hernández.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# As a special exception, the copyright holders give permission to link the
# code of portions of this program with the OpenSSL library under certain
# conditions as described in each individual source file and distribute
# linked combinations including the program with the OpenSSL library. You
# must comply with the GNU Affero General Public License in all respects for
# all of the code used other than as permitted herein. If you modify file(s)
# with this exception, you may extend this exception to your version of the
# file(s), but you are not obligated to do so. If you do not wish to do so,
# delete this exception statement from your version. If you delete this
# exception statement from all source files in the program, then also delete
# it in the license file.
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
        Portfolio(['AAPL', 'GOOG'])
        Portfolio(['AAPL', 'GOOG', 'IBM', 'MSFT', 'ORCL'])

    def test_ctor_assetstr(self):
        """Assets could come as a string."""
        self.assertRaises(ValueError, Portfolio, "")

        Portfolio("AAPL")
        Portfolio("AAPL GOOG")
        Portfolio("AAPL GOOG IBM MSFT ORCL")

    def test_ctor_eqweighted(self):
        """Weights could be passed."""
        assets = "AAPL GOOG IBM MSFT ORCL".split()
        Portfolio(assets)
        # TODO: check if each weight is equal to 1/len(assets)


if __name__ == '__main__':
    unittest.main()

# EOF