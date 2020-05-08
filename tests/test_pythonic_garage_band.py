import pytest
from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band, Musician

def test_version():
    assert __version__ == '0.1.0'

def test_Band():
    beatles = Band("The Beatles",["John Lennon","Paul McCartney","George Harrison"])
    assert beatles.name == "The Beatles"
    assert beatles.members == ["John Lennon","Paul McCartney","George Harrison"]
    assert beatles.play_solos() == "???????"
    assert beatles.__str__() == "Band name is 'The Beatles'; and members of the Band Are: ['John Lennon', 'Paul McCartney', 'George Harrison']"
    assert beatles.__repr__() == "Band(The Beatles,['John Lennon', 'Paul McCartney', 'George Harrison'])"
    assert beatles.to_list() == "The number of Bands created: 1"

def test_Musician():
    with pytest.raises(TypeError):
        Musician("?","?")
   


