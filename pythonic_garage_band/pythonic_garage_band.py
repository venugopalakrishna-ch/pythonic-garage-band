from abc import ABC, abstractmethod

class Band:
    count = 0    
    def __init__(self, name, members, solos):
        self.name = name
        self.members = members   
        self.solos = solos
        Band.count += 1          

    def play_solos(self):         
        play_solos = ""                    
        for obj in self.members:
            play_solos += obj.name.strip("'") + " please play the solo: " + obj.play_solo() + " "
            print(f"{obj.name} please play the solo: {obj.play_solo()}")
        return play_solos.strip()
            
    def __str__(self):
        musicians = ""
        for obj in self.members:
            musicians += obj.name.strip("'") + ", "
        return "Band name is '{}'; and members of the Band Are: {}".format(self.name,musicians.rstrip(", "))

    def __repr__(self):
        return 'Band({},{},{})'.format(self.name,self.members,self.solos)

    def create_from_data(self,path):
        self.path = path
        class_args = []
        musician_args = []
        input = open(self.path )         
        band_name = input.readline()        
        gitar = input.readline().split(":")
        bass = input.readline().split(":")
        drums = input.readline().split(":")
        solos = input.readline().split(":")  
        musician_args.append(Guitarist("'"+gitar[1].strip()+"'"))
        musician_args.append(Bassist("'"+bass[1].strip()+"'"))
        musician_args.append(Drummer("'"+drums[1].strip()+"'"))
        class_args.append(band_name.strip())        
        class_args.append(musician_args)
        class_args.append(solos)            
        return class_args

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
    def __init__(self,name,solo="Sympathy for the Devil"):
        super().__init__(name,"Guitar")
        self.solo = solo

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo

class Bassist(Musician):
    def __init__(self,name,solo="Light My Fire"):
        super().__init__(name,"Bass")
        self.solo = solo

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo

class Drummer(Musician):
    def __init__(self,name,solo="Sharp Dressed Man"):
        super().__init__(name,"Drums")
        self.solo = solo

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return self.solo

if __name__ == "__main__":
     beatles = Band("The Beatles", [Guitarist("John Lennon"), Bassist("Paul McCartney"),Drummer("Siva Mani")],["Sympathy for the Devil","Light My Fire","Sharp Dressed Man"])        
     class_args = beatles.create_from_data("assets/band_input.txt")
     from_file  = Band(class_args[0],class_args[1],class_args[2])
     print(from_file.__repr__())
     print(from_file.__str__())
     solos_test = beatles.play_solos()
         
     

    
    