import datetime

def fight(animal1, animal2):
    if animal1.get_points() > animal2.get_points():
        print("{animal} wins".format(animal = animal1.name))
    elif animal1.get_points() < animal2.get_points():
        print("{animal} wins".format(animal = animal2.name))
    else:
        print("{animal1} and {animal2} are equals".format(animal1 = animal1.name, animal2 = animal2.name))

class Animal:
    """docstring for animal."""
    def __init__(self, name, env, strenth, inteligent, speed,resistence):
        self.name = name
        self.env = env
        self.strenth = strenth
        self.inteligent = inteligent
        self.speed = speed
        self.resistence = resistence
    def name(self):
        return self.name
    def description(self):
        print("Animal: {name}, Environment: {env}, Strenth: {strenth}, Inteligent: {inteligent}, Speed: {speed}, Resistence: {resistence}".format(name = self.name, env = self.env, strenth = str(self.strenth), inteligent = str(self.inteligent), speed = str(self.speed), resistence = str(self.resistence)))
    def get_points(self):
        return self.strenth*self.inteligent + self.speed*self.resistence

duck = Animal("Duck", ['Water', 'Air'], 30, 35, 50, 30)
goose = Animal("Goose", ['Water', 'Air'], 40, 55, 40, 50)
duck.description()
goose.description()

print(duck.get_points())
print(goose.get_points())


fight(duck, goose)
fight(goose, duck)
fight(duck, duck)
fight(goose, goose)
