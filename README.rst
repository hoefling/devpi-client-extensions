devpi-client-extensions
=======================

Some useful stuff around `devpi client`_. Although this package is proudly named *extensions*,
currently there is only one thing implemented ready to be used: a hook that uses passwords from
``.pypirc`` on login to devpi server so you don't have to enter your password if you store it for upload anyway.

Install
-------

.. code-block:: sh

   $ pip install devpi-client-extensions

Usage
-----

Just use the ``devpi login`` command as usual:

.. code-block:: sh

   $ devpi login hoefling
   Using hoefling credentials from .pypirc
   logged in 'hoefling', credentials valid for 10.00 hours

Stats
-----

|pypi| |build| |appveyor| |coverage| |landscape|

.. |pypi| image:: https://badge.fury.io/py/devpi-client-extensions.svg
   :target: https://badge.fury.io/py/devpi-client-extensions
   :alt: Package on PyPI

.. |build| image:: https://travis-ci.org/hoefling/devpi-client-extensions.svg?branch=master
   :target: https://travis-ci.org/hoefling/devpi-client-extensions
   :alt: Build status

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/hoefling/devpi-client-extensions?branch=master&svg=true
   :target: https://ci.appveyor.com/project/hoefling/devpi-client-extensions
   :alt: Windows build status

.. |coverage| image:: https://coveralls.io/repos/github/hoefling/devpi-client-extensions/badge.svg?branch=master
   :target: https://coveralls.io/github/hoefling/devpi-client-extensions?branch=master
   :alt: Coverage status

.. |landscape| image:: https://landscape.io/github/hoefling/devpi-client-extensions/master/landscape.svg?style=flat
   :target: https://landscape.io/github/hoefling/devpi-client-extensions/master
   :alt: Code Health

.. _devpi client: https://github.com/devpi/devpi
