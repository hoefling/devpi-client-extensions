devpi-client-extensions
=======================

Some useful stuff around `devpi client`_. Although this package is proudly named *extensions*,
currently there is only one thing implemented ready to be used: a hook that uses passwords from
``.pypirc`` or `keyring`_ on login to devpi server so you don't have to enter your password
if you store it for upload anyway.

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

Since version 0.3, reading credentials using `keyring`_ is supported. Install the package with `keyring` extras:

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

|pypi| |build| |appveyor| |coverage| |landscape| |requirements| |black|

.. |pypi| image:: https://badge.fury.io/py/devpi-client-extensions.svg
   :target: https://badge.fury.io/py/devpi-client-extensions
   :alt: Package on PyPI

.. |build| image:: https://travis-ci.org/hoefling/devpi-client-extensions.svg?branch=master
   :target: https://travis-ci.org/hoefling/devpi-client-extensions
   :alt: Build status

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/hoefling/devpi-client-extensions?branch=master&svg=true
   :target: https://ci.appveyor.com/project/hoefling/devpi-client-extensions
   :alt: Windows build status

.. |coverage| image:: https://codecov.io/gh/hoefling/devpi-client-extensions/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/hoefling/devpi-client-extensions
   :alt: Coverage status

.. |landscape| image:: https://landscape.io/github/hoefling/devpi-client-extensions/master/landscape.svg?style=flat
   :target: https://landscape.io/github/hoefling/devpi-client-extensions/master
   :alt: Code Health

.. |requirements| image:: https://requires.io/github/hoefling/devpi-client-extensions/requirements.svg?branch=master
     :target: https://requires.io/github/hoefling/devpi-client-extensions/requirements/?branch=master
     :alt: Requirements status

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black

.. _devpi client: https://pypi.org/project/devpi-client/

.. _keyring: https://pypi.org/project/keyring/
