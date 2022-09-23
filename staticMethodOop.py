class Player:
    name  =''
    def __init__(self,name):
        self.name = name


    def getName(self):
        return self.name
    @staticmethod
    def pensiun(age):
        return str(40 - age)



# pemain = Player('Ronaldo')
# print(pemain.getName())

print(f"Pensiun nya {Player.pensiun(27)} tahun lagi" )

