import pytest
from string_utils import StringUtils
# Функция 1
@pytest.mark.positive
@pytest.mark.parametrize( "text_vvod, text_result", [
    ("hello","Hello"),
    ("Hello","Hello" ),
    ("hello my friends","Hello my friends")
])
def test_positiv_capitalize(text_vvod, text_result):
    capital = StringUtils()
    assert capital.capitalize(text_vvod) == text_result

@pytest.mark.negative
@pytest.mark.parametrize( "text_vvod, text_result", [
    (" "," "),
    ("123fa","123fa" ),
    ("","")
])
def test_negativ_capitalize(text_vvod, text_result):
    capital = StringUtils()
    assert capital.capitalize(text_vvod) == text_result

# Функция 2
@pytest.mark.positive
@pytest.mark.parametrize( "text_vvod, text_result", [
    ("  hello","hello"),
    ("hello","hello" ),
    ("  hello my friends","hello my friends")
])
def test_positiv_trim(text_vvod, text_result):
    tr = StringUtils()
    assert tr.trim(text_vvod) == text_result

@pytest.mark.negative
@pytest.mark.parametrize( "text_vvod, text_result", [
    ("  ",""),
    ("","" ),
])
def test_negative_trim(text_vvod, text_result):
    tr = StringUtils()
    assert tr.trim(text_vvod) == text_result
# Функция 3
@pytest.mark.positive
@pytest.mark.parametrize( "text_vvod, simvol", [
    ("hello","h"),
    ("hello","e" ),
    ("hell21","2")
])
def test_positiv_contains(text_vvod, simvol):
    cont = StringUtils()
    otv = cont.contains(text_vvod, simvol)
    assert otv

@pytest.mark.negative
@pytest.mark.parametrize( "text_vvod, simvol", [
    ("hello"," h" ),
    ("hello","H"),
    ("123","4")
])
def test_negative_contains(text_vvod, simvol):
    cont = StringUtils()
    otv = cont.contains(text_vvod, simvol)
    assert not otv
# Функция 4

@pytest.mark.positive
@pytest.mark.parametrize( "text_vvod, simvol, text_result ", [
    ("hello","h", "ello"),
    ("hello","l", "heo"),
    ("12345","4", "1235"),
    ("hell o"," ", "hello")
])
def test_positiv_delete_symbol(text_vvod, simvol, text_result):
    cont = StringUtils()
    otv = cont.delete_symbol(text_vvod, simvol)
    assert otv == text_result

@pytest.mark.negative
@pytest.mark.parametrize( "text_vvod, simvol, text_result ", [
    ("hello my friends","freins", "hello my friends"),
    ("hello","H", "hello"),
    ("","", "")
])
def test_negative_delete_symbol(text_vvod, simvol, text_result):
    cont = StringUtils()
    otv = cont.delete_symbol(text_vvod, simvol)
    assert otv == text_result