try:
    import pathlib
except ImportError:
    import pathlib2 as pathlib
from readme_renderer.rst import render


def test_markup_is_generated():
    readme = pathlib.Path('README.rst')
    with readme.open() as f:
        assert render(f.read()) is not None
