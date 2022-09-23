class Player:
    name =''
    speed = ''
    def __init__(self,name,speed):
        self.name
        self.speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed


class Age(Player):
    def setAge(self,age):
        self.age = age
        return self.age


pemain = Age('Ronaldino','94')
pemain2 = Age('Messi','95')

print(f'{pemain.getName()} Umurnya {pemain.setAge("28")} punya speed {pemain.getSpeed()}')

