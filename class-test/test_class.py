import pytest

class TestClass(object):
    def test_one(self):
        x = "this"
        # Spytest.set_trace() # invoke debugger
        assert 'h' in x

    def test_two(self):
        assert 2 == 1+1    