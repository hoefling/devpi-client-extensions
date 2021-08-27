devpi-client-extensions
=======================

Some useful stuff around `devpi client`_. Although this package is proudly named
*extensions*, currently there is only one thing implemented ready to be used:
a hook that uses passwords from ``.pypirc`` or `keyring`_ on login to devpi server
so you don't have to enter your password if you store it for upload anyway.

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

Keyring Support
---------------

Since version 0.3, reading credentials using `keyring`_ is supported.
Install the package with ``keyring`` extras:

.. code-block:: sh

   $ pip install devpi-client-extensions[keyring]

Example with storing the password in keyring:

.. code-block:: sh

   $ keyring set https://my.devpi.url/ hoefling
   $ devpi login hoefling
   Using hoefling credentials from keyring
   logged in 'hoefling', credentials valid for 10.00 hours

Stats
-----

|pypi| |build| |coverage| |black| |precommit|

.. |pypi| image:: https://img.shields.io/pypi/v/devpi-client-extensions.svg?logo=python&logoColor=white
   :target: https://pypi.python.org/pypi/devpi-client-extensions
   :alt: Package on PyPI

.. |build| image:: https://github.com/hoefling/devpi-client-extensions/workflows/CI/badge.svg
   :target: https://github.com/hoefling/devpi-client-extensions/actions?query=workflow%3A%22CI%22
   :alt: Build status on Github Actions

.. |coverage| image:: https://codecov.io/gh/hoefling/devpi-client-extensions/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/hoefling/devpi-client-extensions
   :alt: Coverage status

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black

.. |precommit| image:: https://results.pre-commit.ci/badge/github/hoefling/devpi-client-extensions/master.svg
   :target: https://results.pre-commit.ci/latest/github/hoefling/devpi-client-extensions/master
   :alt: pre-commit.ci status

.. _devpi client: https://pypi.org/project/devpi-client/

.. _keyring: https://pypi.org/project/keyring/
