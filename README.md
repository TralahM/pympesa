
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

# Description
This is an unofficial wrapper providing convenient access to the Safaricom MPESA Daraja API for applications written in Python.

It has been tested with Python 2 & 3

### Setup and Installation

```Bash
pip install daraja-mpesa
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
from mpesa.api.<API> import <API Class>
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



[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge)](https://github.com/TralahM)

# Documentation

[Read the Docs](https://pympesa.readthedocs.io)
# Dependencies

# How to Install


## Building from Source for Developers

```Bash
git clone https://github.com/TralahM/pympesa.git
cd pympesa
python setupy bdist_wheel
python setupy install
```

# Contributing
[See the Contributing File](CONTRIBUTING.rst)


[See the Pull Request File](PULL_REQUEST_TEMPLATE.md)

# Support

# LICENCE
[Read the license here](LICENSE)


# Acknowledgements


