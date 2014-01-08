The Rixnik Project
==================

Welcome to the **Rixnik Project**!

DISCLAIMER
----------

Maybe in the future, some pieces of this code could be useful for a newbie, but meanwhile, please you should be careful about this statement:

> This code is been written by a student, not a professional quant. So, **YOU CAN USE IT BUT AT YOUR OWN RISK**.

About the project
-----------------

After following -through [Coursera]-, a course from Prof. [Zivot]'s named [Introduction to Computational Finance and Financial Econometrics][1], I found that something was missing: my own code!

[Coursera]: http://coursera.org "Coursera.org"
[Zivot]: http://faculty.washington.edu/ezivot/ "Eric Zivot's UW Homepage"

[1]: https://www.coursera.org/course/compfinance "Introduction to Computational Finance and Financial Econometrics"

This project was first, an attempt to make my own follow-up trying to write some [Python] code for portfolio management and analysis. But later, when I was taking another course: [Computational Investing, Part I][2] from Prof. [Balch], my code was in a way that may be a different direction.

So, I feel that I need to take things with a better approach and rewrite this from scratch. This incarnation of **Rixnik** (at [GitHub]) is that rewrite!

[Python]: http://www.python.org "Python Programming Language"
[Balch]: http://www.cc.gatech.edu/~tucker/ "Tucker Balch's homepage"
[GitHub]: http://github.com "GitHub"

[2]: https://www.coursera.org/course/compinvesting1 "Computational Investing, Part I"

Current status
--------------

Right now, I'm trying to define some data structures (using [pandas]), to represent portfolio data from Zivot's code and [PerformanceAnalytics]. This is stuff will be located in the package `rixnik.data`. You can take a look to the package `test.data` for a basic test suite, or use:

~~~~
nosetests
~~~~

from your working clone to run all its test suite.

[pandas]: http://pandas.pydata.org/ "pandas - Python Data Analysis Library"
[PerformanceAnalytics]: http://cran.r-project.org/web/packages/PerformanceAnalytics/ "PerformanceAnalytics: Econometric tools for performance and risk analysis"

The repository
--------------

Initially, this code was hosted at [Google Code], but now the original repository is a mirror and the updated repository is and will be at *GitHub*. So, feel free to run:

~~~~
git clone https://github.com/tnotstar/rixnik
~~~~

[Google Code]: http://code.google.com/p/rixnik "Rixnik at Google Code"

License
-------

Finally, **Rixnik** is a free and open source project, and it's made available under the terms of the [GNU Affero General Public License (AGPL)][3].

[3]: http://www.gnu.org/licenses/agpl-3.0.html "GNU Affero General Public License (AGPL)"
