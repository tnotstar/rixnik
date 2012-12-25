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
This module declares the data structures used to work with a portfolio
of assets.
"""

import numpy as np
import pandas as pd
import datetime as dt


class Portfolio(object):
    """Represents a portfolio of assets."""

    def __init__(self, assets, weights=None, date=None):
        """Initializes the given portfolio with a list of assets and
           optionally, a weights vector and a reference date."""

        # if assets are given as string, split them first
        if isinstance(assets, basestring):
            assets = assets.split()

        # check correct type and values for assets
        if not isinstance(assets, (list, set, tuple)):
            msg = "assets must to be a list, a set or a tuple"
            raise TypeError(msg)

        assets_nr = len(assets)
        if not assets_nr > 0:
            msg = "needed at least one asset, given {}".format(assets_nr)
            raise ValueError(msg)

        # if weights aren't given, assume it's equally weighted portfolio
        if weights is None:
            weights = [1.0/assets_nr] * assets_nr

        # check correct type and values for weights
        if not isinstance(weights, (list, tuple)):
            msg = "weights must to be a list or tuple"
            raise TypeError(msg)
        if assets_nr != len(weights):
            msg = "expecting a weights vector of length {}".format(assets_nr)
            raise ValueError(msg)

        weights_sm = sum(weights)
        if weights_sm > 1.0:
            msg = "weights cannot exceed from 1.0, but its sum is {}". \
                format(weights_sm)
            raise ValueError(msg)

        # if date isn't given, assume it's today
        if date is None:
            date = dt.datetime.combine(dt.date.today(), dt.time())

        # check correct type for the reference date
        if not isinstance(date, dt.datetime):
            msg = "expecting a `datetime` instance for the reference date"
            raise TypeError(msg)

        # initializes the internal data frame
        self._data = pd.DataFrame(np.array([weights]), columns=assets,
                index=[date])

# EOF
