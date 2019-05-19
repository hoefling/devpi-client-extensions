import io
import os
import setuptools_scm
import toml


# CI=true is supported by at least Gitlab, Travis and Appveyor
if __name__ == '__main__' and os.environ.get('CI', None):
    conf = os.path.normpath(os.path.join(__file__, '..', '..', 'pyproject.toml'))
    with io.open(conf, encoding='utf-8') as fp:
        d = toml.load(conf)
    d['tool']['poetry']['version'] = setuptools_scm.get_version()
    with io.open(conf, mode='w', encoding='utf-8') as fp:
        toml.dump(d, fp)
