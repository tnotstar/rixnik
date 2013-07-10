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