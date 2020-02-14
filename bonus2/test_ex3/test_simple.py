
def my_add(x, y):
    return x + y

def my_mul(x, y):
    return x * y

def test_my_add():
    assert(my_add(1, 1) == 2)
    assert(my_add(5, 6) == 11)

def test_my_mul():
    assert(my_mul(5, 5) == 25)
    assert(my_mul(1, 5) == 5)
