'''

BELAJAR MEMBUAT CLASS DI PYTHON
'''

class Player:
    name ="Wakijo"
    def getName(self,nama):
        self.name = nama
        return self.name


pemain1 = Player()
pemain2 = Player()

print(pemain1.getName("Warjono"))
print(pemain2.getName("Marjono"))
