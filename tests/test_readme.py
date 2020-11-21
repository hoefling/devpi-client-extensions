from io import StringIO  # python3

from readme_renderer.rst import render


def test_markup_is_generated():
    warnings = StringIO()
    with open('README.rst') as f:
        html = render(f.read(), stream=warnings)
        warnings.seek(0)
        assert html is not None, warnings.read()
