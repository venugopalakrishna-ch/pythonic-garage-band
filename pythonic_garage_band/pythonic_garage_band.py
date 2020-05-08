from abc import ABC, abstractmethod

class Band:
    count = 0
    def __init__(self, name, members):
        self.name = name
        self.members = members   
        Band.count += 1          

    def play_solos(self):    
        return "???????"

    def __str__(self):
        return "Band name is '{}'; and members of the Band Are: {}".format(self.name,self.members)

    def __repr__(self):
        return 'Band({},{})'.format(self.name,self.members)

    @classmethod
    def to_list(cls):        
        return f"The number of Bands created: {cls.count}"      


class Musician(ABC):
    def __init__(self,name,instrument):
        self.name = name
        self.instrument = instrument
    
    def __str__(self):
        return "{} plays {}".format(self.name,self.instrument)

    def __repr__(self):
        return 'Musician({},{})'.format(self.name,self.instrument)

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


    