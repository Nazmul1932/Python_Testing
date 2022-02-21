import pytest

def test_m1():
    a=3
    b=4
    assert a+1 == b, "test failed"
    assert a == b, "test failed"
    
def test_m2():
    name = 'pytest'
    assert name.upper() == 'PYTEST'
    
def test_m3():
    assert True

@pytest.mark.login      
def test_login():
    assert 'admin'=='admin'
    