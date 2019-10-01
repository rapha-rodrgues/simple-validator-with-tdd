from main import validate_code


def test_invalid_type_input():
    assert not validate_code('abcdef')
    assert not validate_code('XYZASD')
    assert not validate_code('123ABC')


def test_invalid_length():
    assert not validate_code('0123456789')
    assert not validate_code('01234')


def test_invalid_range_value():
    assert not validate_code('000000')
    assert not validate_code('012345')
    assert not validate_code('099999')


def test_invalid_repeated_number():
    assert not validate_code('121426')
    assert not validate_code('552523')
    assert not validate_code('122131')


def test_valid_code():
    assert validate_code('523563')
    assert validate_code('112233')
    assert validate_code('123123')

