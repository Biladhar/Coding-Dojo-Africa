class Ninja:
    def __init__(self,first_name,last_name,treats,pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self
    # def display_info_ninja(self):
    #     print(f' name: {self.first_name} \n last name: {self.last_name} \n treats: {self.treats} \n pet food: {self.pet_food} \n pet: {self.pet.name}' )       # for test


class Pet:
    def __init__(self,name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 10
        self.energy = 10
    def sleep(self):
        self.energy += 25
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        return self
    def play(self):
        self.health += 5
        return self
    def noise(self):
        print('pikapi')
        return self
    # def display_info_pet(self):
    #     print(f' name: {self.name} \n type: {self.type} \n tricks: {self.tricks} \n health: {self.health} \n energy: {self.energy}' )     #for test



pikatchu = Pet("Pikatchu","pokemon","elektroChock")
Trump = Ninja("Donald","Trump",100, 100,pikatchu)



Trump.feed().walk().bathe()






# Trump.display_info_ninja()                        #for test
# print("="*20)
# pikatchu.display_info_pet()






























