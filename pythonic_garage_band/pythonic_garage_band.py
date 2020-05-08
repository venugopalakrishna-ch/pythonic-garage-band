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

class Guitarist(Musician):
    def __init__(self,name):
        super().__init__(name,"Guitar")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "Sympathy for the Devil"

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name,"Bass")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "Light My Fire"

class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name,"Drums")

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return "Sharp Dressed Man"

    


    