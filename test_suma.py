from test_suma import sumar  # ← Importación normal

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(0, 0) == 0
    assert sumar(-1, 1) == 0
    assert sumar(10, 20) == 30