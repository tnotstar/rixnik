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
This module declares the data structures used to work with
a portfolio of assets.
"""

from dateutil.parser import parse as parsedate

import numpy as np
import pandas as pd
import datetime as dt


class Portfolio(object):
    """Represents a portfolio of assets."""

    def __init__(self, assets, weights=None, date=None):
        """Initializes the given portfolio with a list of assets and
           optionally, a weights vector and a reference date."""

        # if assets are given inside a string, split them first
        if isinstance(assets, str):
            assets = assets.split()

        # cast assets to a list, whenever the object is iterable
        try:
            assets = [a for a in assets]
        except TypeError:
            raise TypeError("assets must to be an iterable object")

        assets_nr = len(assets)
        if not assets_nr > 0:
            raise ValueError("needed at least one asset, given {0}". \
                format(assets_nr))

        # if weights aren't given, assume it's equally weighted portfolio
        if weights is None:
            weights = [1.0/assets_nr  for _ in assets]

        # cast weights to a list, whenever the object is iterable
        try:
            weights = [w for w in weights]
        except TypeError:
            raise TypeError("weights must to be an iterable object")

        if assets_nr != len(weights):
            raise ValueError("expecting a weights vector of length {0}". \
                format(assets_nr))

        if sum(weights) > 1.0:
            raise ValueError("weights cannot exceed 1.0, but its sum is {0}". \
                format(weights_sm))

        # if date isn't given, assume it is today
        if date is None:
            date = dt.datetime.combine(dt.date.today(), dt.time())

        # if date is a string, try to parse it
        if isinstance(date, str):
            date = parsedate(date)

        # check if the type of reference date is `datetime`
        if not isinstance(date, dt.datetime):
            raise TypeError("expecting a `datetime` instance for " +
                "the reference date")

        # initializes the internal data frame
        self._data = pd.DataFrame(np.array([weights]), columns=assets,
                index=[date])

# EOF