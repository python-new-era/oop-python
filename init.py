class Player:
    name =''
    speed = ''

    def __init__(self,name,speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed


pemain1 = Player('Messi' , 92)
pemain2 = Player('Rondaldo',91)

print(f"{pemain1.getName()} Punya Speed {pemain1.getSpeed()}")
print(f"{pemain2.getName()} Punya Speed {pemain2.getSpeed()}" )


