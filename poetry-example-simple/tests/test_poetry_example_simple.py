from unittest import TestCase
from poetry_example_simple import __version__


class TestModuleRoot(TestCase):
    def test_version(self):
        assert __version__ == '0.1.0'
