import os
import setuptools_scm
import toml


if __name__ == '__main__' and os.getenv('TRAVIS', None):
    conf = os.path.normpath(os.path.join(__file__, '..', '..', 'pyproject.toml'))
    d = toml.load(conf)
    d['tool']['poetry']['version'] = setuptools_scm.get_version()
    with open(conf, 'w') as fp:
        toml.dump(d, fp)
