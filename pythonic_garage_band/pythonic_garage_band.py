
class Band:
    count = 0
    def __init__(self, name, members):
        self.name = name
        self.members = members   
        Band.count += 1          

    def play_solo(self):    
        return "???????"

    def __str__(self):
        return "Band name is '{}'; and members of the Band Are: {}".format(self.name,self.members)

    def __repr__(self):
        return 'Band({},{})'.format(self.name,self.members)

    @classmethod
    def to_list(cls):        
        return f"The number of Bands created: {cls.count}"        

    