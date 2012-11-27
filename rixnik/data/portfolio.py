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
"""
This module declares the data structures used to work with a portfolio of
different assets.
"""

import pandas as p


class Portfolio(p.DataFrame):
    """TODO"""

    def __init__(self, title, frame=None):
        super(Portfolio, self).__init__()
        self._title = title

    @property
    def title(self):
        """A getter method for the portfolio title."""
        return self._title

# EOF