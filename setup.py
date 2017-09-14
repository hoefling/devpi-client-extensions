from io import open
from setuptools import setup, find_packages
from devpi_ext import __version__


with open('README.rst', mode='r', encoding='utf8') as file:
    README = file.read()
with open('LICENSE', mode='r', encoding='utf8') as file:
    LICENSE = file.read()


def classifiers():
    """builds list of trove classifiers"""
    common = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: Implementation',
    ]
    py_versions = [
        'Programming Language :: Python :: {}'.format(ver)
        for ver in ['2.7', '3.4', '3.5', '3.6']
    ]
    return common + py_versions


setup(
    name='devpi-client-extensions',
    description='devpi client extensions',
    long_description=README,
    license=LICENSE,
    version=__version__,
    packages=find_packages(),
    install_requires=['devpi-client>=3.0.0'],
    url='https://github.com/hoefling/devpi-client-extensions',
    maintainer='Oleg Hoefling',
    maintainer_email='oleg.hoefling@gmail.com',
    classifiers=classifiers(),
    entry_points={
        'devpi_client': ['devpi-client-ext-login = devpi_ext.login']
    }
)
