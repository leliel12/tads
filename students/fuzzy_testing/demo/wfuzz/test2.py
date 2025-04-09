def suma(a, b):
    if a < 0 and b < 0:
        return 0
    return a + b

from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_suma_property(a, b):
    assert suma(a, b) == a + b
    
# pytest test2.py