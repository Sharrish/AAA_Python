import pytest
from morse import decode


@pytest.mark.parametrize('morse_code,morse_decode', [
    ('... --- ...', 'SOS'),
    ('... .- .. -', 'SAIT'),
    ('', ''),
])
def test_decode(morse_code, morse_decode):
    assert decode(morse_code) == morse_decode
