# pyre-strict


__all__ = ['__version__']


def _read_version():
    try:  # reading the version from installation metadata
        from pkg_resources import DistributionNotFound, get_distribution

        return get_distribution('devpi-client-extensions').version
    except (ImportError, DistributionNotFound):
        return 'UNKNOWN'


__version__ = _read_version()
