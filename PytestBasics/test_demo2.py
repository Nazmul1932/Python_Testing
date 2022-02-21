import pytest

def test_m4():
    assert False

@pytest.mark.home        
def test_m5():
    assert 100 == 100

@pytest.mark.home    
def test_m6():
    assert 'nazmul' == 'NAZMUL'

@pytest.mark.login      
def test_login():
    assert 'admin'=='admin3'