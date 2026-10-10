from password_checker import is_strong

def test_weak_password_too_short():
    assert is_strong("abc") == False

def test_weak_password_no_digit():
    assert is_strong("Abcdefgh!") == False

def test_weak_password_no_upper():
    assert is_strong("abcdefg1!") == False

def test_weak_password_no_lower():
    assert is_strong("ABCDEFG1!") == False

def test_weak_password_no_symbol():
    assert is_strong("Abcdefg1") == False

def test_strong_password():
    assert is_strong("Abcdef1!") == True