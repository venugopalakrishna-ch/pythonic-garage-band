import pytest
from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band, Musician, Guitarist, Bassist, Drummer

def test_version():
    assert __version__ == '0.1.0'

def test_band():
    beatles = Band("The Beatles",["John Lennon","Paul McCartney","George Harrison"],["Sympathy for the Devil","Light My Fire","Sharp Dressed Man"])
    assert beatles.name == "The Beatles"
    assert beatles.members == ["John Lennon","Paul McCartney","George Harrison"]                   
    assert beatles.__repr__() == "Band(The Beatles,['John Lennon', 'Paul McCartney', 'George Harrison'],['Sympathy for the Devil', 'Light My Fire', 'Sharp Dressed Man'])"
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


def test_some_band(some_band):
    assert some_band.name == "The Beatles" 
    assert some_band.to_list() == "The number of Bands created: 2" 
    assert some_band.__str__() == "Band name is 'The Beatles'; and members of the Band Are: John Lennon, Paul McCartney, Siva Mani"
    assert some_band.__repr__() == "Band(The Beatles,[Musician(John Lennon,Guitar), Musician(Paul McCartney,Bass), Musician(Siva Mani,Drums)],['Sympathy for the Devil', 'Light My Fire', 'Sharp Dressed Man'])"
    assert some_band.play_solos() == "John Lennon please play the solo: Sympathy for the Devil Paul McCartney please play the solo: Light My Fire Siva Mani please play the solo: Sharp Dressed Man"    
    class_args = some_band.create_from_data("pythonic_garage_band/assets/band_input.txt")
    from_data  = Band(class_args[0],class_args[1],class_args[2])
    assert from_data.name == "The Beatles"
    assert from_data.to_list() == "The number of Bands created: 3" 
    assert from_data.__str__() == "Band name is 'The Beatles'; and members of the Band Are: John Lennon, Paul McCartney, Siva Mani"    
    assert from_data.__repr__() == "Band(The Beatles,[Musician('John Lennon',Guitar), Musician('Paul McCartney',Bass), Musician('Siva Mani',Drums)],['Sympathy for the Devil', 'Light My Fire', 'Sharp Dressed Man'])"
    assert from_data.play_solos() == "John Lennon please play the solo: Sympathy for the Devil Paul McCartney please play the solo: Light My Fire Siva Mani please play the solo: Sharp Dressed Man"    

@pytest.fixture
def some_band():
    beatles = Band("The Beatles", [Guitarist("John Lennon"), Bassist("Paul McCartney"),Drummer("Siva Mani")],["Sympathy for the Devil","Light My Fire","Sharp Dressed Man"])
    return beatles