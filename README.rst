devpi-client-extensions
=======================

Some useful stuff around `devpi client`_. Although this package is proudly named *extensions*,
currently there is only one thing implemented ready to be used: a hook that uses passwords from
``.pypirc`` on login to devpi server so you don't have to enter your password if you store it for upload anyway.

.. code-block:: sh

   $ devpi login hoefling
   Using hoefling credentials from .pypirc
   logged in 'hoefling', credentials valid for 10.00 hours

Stats
-----
|build| |appveyor| |coverage|

.. |build| image:: https://travis-ci.org/hoefling/devpi-client-extensions.svg?branch=master
   :target: https://travis-ci.org/hoefling/devpi-client-extensions
   :alt: Build status

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/hoefling/devpi-client-extensions?branch=master&svg=true
   :target: https://ci.appveyor.com/project/hoefling/devpi-client-extensions
   :alt: Windows build status

.. |coverage| image:: https://coveralls.io/repos/github/hoefling/devpi-client-extensions/badge.svg?branch=master
   :target: https://coveralls.io/github/hoefling/devpi-client-extensions?branch=master
   :alt: Coverage status

.. _devpi client: https://github.com/devpi/devpi
