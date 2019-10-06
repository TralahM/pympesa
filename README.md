
[![Build Status](https://travis-ci.com/TralahM/pympesa.svg?branch=master)](https://travis-ci.com/TralahM/pympesa)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)
[![Organization](https://img.shields.io/badge/Org-TralahTek-blue.svg)](https://github.com/TralahTek)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![HitCount](http://hits.dwyl.io/TralahM/pympesa.svg)](http://dwyl.io/TralahM/pympesa)
[![Inline Docs](http://inch-ci.org/github/TralahM/pympesa.svg?branch=master)](http://inch-ci.org/github/TralahM/pympesa)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/TralahM/pull/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/Naereen/StrapDown.js.svg)](https://gitHub.com/TralahM/pympesa/pull/)
[![GitHub version](https://badge.fury.io/gh/Naereen%2FStrapDown.js.svg)](https://github.com/TralahM/pympesa).

# pympesa.


[![TralahM](https://img.shields.io/badge/Developer-TralahM-blue.svg?style=for-the-badge)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge)](https://github.com/TralahM)

This is an unofficial wrapper providing convenient access to the Safaricom MPESA Daraja API for applications written in Python.

It has been tested with Python 2 & 3

### Setup and Installation

```Bash
pip install pympesa
```
You can also clone or download the library package and install it using setuptools:
``` bash
git clone https://github.com/TralahM/pympesa.git
cd pympesa
python setup.py install
```

### Tests
The library comes with simple integration tests with Safaricom's sandbox APIs. Due to factors beyond my control, the tests are structured to pass even when a specific Daraja API is under maintenance. To run the tests, simply execute pytest from the library's root directory:

``` bash
pytest
```

### Usage

``` python
from pympesa.api.<API> import <API Class>
```
***API***
The following APIs are supported:
-   transaction_status
-   mpesa_express
-   reversal
-   balance
-   auth
-   b2c
-   c2b
-   b2b

***API Class***
The following are the corresponding API classes:
 - TransactionStatus
 - MpesaExpress
 - Reversal
 - Balance
 - MpesaBase
 - B2B
 - C2B
 - B2C


### Documentation

For more information about the modules and APIs, please see the [documentation](https://pympesa.readthedocs.io/).

## Scripts Herein.

* [setup.py](https://github.com/TralahM/pympesa/blob/master/setup.py)

* [oldRme.md](https://github.com/TralahM/pympesa/blob/master/oldRme.md)

* [mpesa](https://github.com/TralahM/pympesa/blob/master/mpesa)

* [LICENSE](https://github.com/TralahM/pympesa/blob/master/LICENSE)

* [requirements.txt](https://github.com/TralahM/pympesa/blob/master/requirements.txt)

* [CONTRIBUTING.rst](https://github.com/TralahM/pympesa/blob/master/CONTRIBUTING.rst)

* [README.md](https://github.com/TralahM/pympesa/blob/master/README.md)

* [docs](https://github.com/TralahM/pympesa/blob/master/docs)

* [CODE_OF_CONDUCT.md](https://github.com/TralahM/pympesa/blob/master/CODE_OF_CONDUCT.md)

# Contributors.

* [TralahTek](https://github.com/TralahTek)
* [TralahM](https://github.com/TralahM)
