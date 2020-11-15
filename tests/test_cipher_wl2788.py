from cipher_wl2788 import __version__
from cipher_wl2788 import cipher_wl2788

def test_version():
    assert __version__ == '0.1.0'
    
def test_cipher_with_single_word():
    expected = "ibqqz"
    actual = cipher_wl2788.cipher("happy", 1, True)
    assert actual == expected