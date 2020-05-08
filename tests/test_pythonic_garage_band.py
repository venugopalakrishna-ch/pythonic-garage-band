import pytest
from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band, Musician, Guitarist, Bassist, Drummer

def test_version():
    assert __version__ == '0.1.0'

def test_band():
    beatles = Band("The Beatles",["John Lennon","Paul McCartney","George Harrison"])
    assert beatles.name == "The Beatles"
    assert beatles.members == ["John Lennon","Paul McCartney","George Harrison"]
    assert beatles.play_solos() == "???????"
    assert beatles.__str__() == "Band name is 'The Beatles'; and members of the Band Are: ['John Lennon', 'Paul McCartney', 'George Harrison']"
    assert beatles.__repr__() == "Band(The Beatles,['John Lennon', 'Paul McCartney', 'George Harrison'])"
    assert beatles.to_list() == "The number of Bands created: 1"

def test_musician():
    with pytest.raises(TypeError):
        Musician("?","?")

def test_guiterist():
    john = Guitarist("John Lennon")
    assert john.name == "John Lennon"
    assert john.get_instrument() == "Guitar"
    assert john.play_solo() == "Sympathy for the Devil"
    assert john.__str__() == "John Lennon plays Guitar"
    assert john.__repr__() == "Musician(John Lennon,Guitar)"

def test_bassist():
    paul = Bassist("Paul McCartney")
    assert paul.name == "Paul McCartney"
    assert paul.get_instrument() == "Bass"
    assert paul.play_solo() == "Light My Fire"
    assert paul.__str__() == "Paul McCartney plays Bass"
    assert paul.__repr__() == "Musician(Paul McCartney,Bass)"

def test_drummer():
    siva = Drummer("Siva Mani")
    assert siva.name == "Siva Mani"
    assert siva.get_instrument() == "Drums"
    assert siva.play_solo() == "Sharp Dressed Man"
    assert siva.__str__() == "Siva Mani plays Drums"
    assert siva.__repr__() == "Musician(Siva Mani,Drums)"


   


