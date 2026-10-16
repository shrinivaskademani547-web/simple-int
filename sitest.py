from simpleint import simple_intrest

def test_normal():
    assert simple_interest(10000, 5, 2) == 100

def test_zero_rate():
    assert simple_intrest(1000, 0, 3) == 0    

def test_zero_time():
    assert simple_intrest(1000, 7, 0) == 0

def test_decimal():
    assert simple_intrest(1000, 2.5, 2) == 50