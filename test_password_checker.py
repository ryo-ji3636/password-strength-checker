from password_checker import is_strong

def test_weak_password_too_short():
    strong, reasons = is_strong("abc")
    assert strong == False
    assert "too short" in reasons

def test_weak_password_no_digit():
    strong, reasons = is_strong("Abcdefgh!")
    assert strong == False
    assert "missing a digit" in reasons

def test_weak_password_no_upper():
    strong, reasons = is_strong("abcdefg1!")
    assert strong == False
    assert "missing an uppercase letter" in reasons

def test_weak_password_no_lower():
    strong, reasons = is_strong("ABCDEFG1!")
    assert strong == False
    assert "missing a lowercase letter" in reasons

def test_weak_password_no_symbol():
    strong, reasons = is_strong("Abcdefg1")
    assert strong == False
    assert "missing a symbol" in reasons

def test_strong_password():
    strong, reasons = is_strong("Abcdef1!")
    assert strong == True
    assert reasons == []