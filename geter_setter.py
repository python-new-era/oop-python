class Player:
    name = ''
    age =''
    info = ''

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    @property
    def infoPlayer(self):
        return self.name + 'adalah ' + self.age

    @infoPlayer.setter
    def infoPlayer(self,data):
        name ,age = data.split(" ")
        self.name = name
        self.age = age

pemain = Player('Ronaldo','23')
pemain.infoPlayer("adalah 23")

print(pemain.infoPlayer)