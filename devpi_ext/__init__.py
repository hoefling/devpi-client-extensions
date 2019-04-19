import os

from pkg_resources import DistributionNotFound, get_distribution


def _read_version():  # pragma: no cover
    try:  # reading the version from installation metadata
        return get_distribution('devpi-client-extensions').version
    except DistributionNotFound:
        pass
    try:  # falling back to setuptools-scm
        from setuptools_scm import get_version

        return get_version(root=os.pardir, relative_to=__file__)
    except ImportError:
        return 'UNKNOWN'


__version__ = _read_version()
