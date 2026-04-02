class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self._age = age

    def roar(self):
        print(f"{self.name} ROARS!")

    def eat(self, food):
        if food.lower() == self.diet.lower():
            print(f"{self.name} eats the {food}.")
        else:
            print(f"{self.name} doesn’t eat {food}.")

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Invalid age!")

    def info(self):
        print(f"Name: {self.name}, Species: {self.species}, Diet: {self.diet}, Age: {self._age}")

class FlyingDinosaur(Dinosaur):
    def __init__(self, name, species, diet, age, wing_span):
        super().__init__(name, species, diet, age)
        self.wing_span = wing_span

    def roar(self):
        print(f"{self.name} SCREECHES!")

    def fly(self):
        print(f"{self.name} flies with a wingspan of {self.wing_span} meters!")

class WaterDinosaur(Dinosaur):
    def __init__(self, name, species, diet, age, swim_speed):
        super().__init__(name, species, diet, age)
        self.swim_speed = swim_speed

    def roar(self):
        print(f"{self.name} ROARS underwater!")

    def swim(self):
        print(f"{self.name} swims at {self.swim_speed} mph!")

bob = Dinosaur("Bob", "T-Rex", "Meat", 20)
lizzy = FlyingDinosaur("Lizzy", "Pterodactyl", "Meat", 7, 12)
sam = WaterDinosaur("Sam", "Plesiosaur", "Fish", 10, 8)

dinosaurs = {"1": bob, "2": lizzy, "3": sam}

food_options = ["Meat", "Plants", "Fish", "Fruit"]

print("Pick a dinosaur (1-Bob, 2-Lizzy, 3-Sam):")
choice = input()

if choice in dinosaurs:
    dino = dinosaurs[choice]
    dino.info()
    dino.roar()
    if hasattr(dino, "fly"):
        dino.fly()
    if hasattr(dino, "swim"):
        dino.swim()

    print("Choose food to feed the dinosaur:")
    for i, food in enumerate(food_options, 1):
        print(f"{i}. {food}")
    food_choice = input("Enter the number of the food: ")

    if food_choice.isdigit() and 1 <= int(food_choice) <= len(food_options):
        selected_food = food_options[int(food_choice)-1]
        dino.eat(selected_food)
    else:
        print("Invalid food choice.")
else:
    print("Invalid dinosaur choice.")