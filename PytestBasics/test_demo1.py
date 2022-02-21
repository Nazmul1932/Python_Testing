import pytest

@pytest.mark.login
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
def test_m4():
    assert False
    
def test_m5():
    assert 100 == 100
    
def test_m6():
    assert 'nazmul' == 'NAZMUL'

@pytest.mark.login    
def test_login():
    assert 'admin'=='admin'
    
