devpi-client-extensions
=======================

Some useful stuff around `devpi client`_. Although this package is proudly named *extensions*,
currently there is only one thing implemented ready to be used: a hook that uses passwords from
``.pypirc`` on login to devpi server so you don't have to enter your password if you store it for upload anyway.

.. code-block:: sh

   $ devpi login hoefling
   Using hoefling credentials from .pypirc
   logged in 'hoefling', credentials valid for 10.00 hours

.. _devpi client: https://github.com/devpi/devpi
