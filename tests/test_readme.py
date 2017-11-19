from readme_renderer.rst import render


def test_markup_is_generated():
    with open('README.rst') as f:
        assert render(f.read()) is not None
