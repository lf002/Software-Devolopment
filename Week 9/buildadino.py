class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age

    def roar(self):
        print(f"{self.name} lets out a mighty ROAR!")

    def eat(self, food):
        if food == self.diet:
            print(f"{self.name} happily eats the {food}.")
        else:
            print(f"{self.name} doesn’t eat {food}.")

    def dino_info(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Diet: {self.diet}")

rex = Dinosaur("Rex", "Tyrannosaurus Rex", "Meat", 19)
trice = Dinosaur("Trice", "Triceratops", "Plants", 13)
velo = Dinosaur("Velo", "Velociraptor", "Meat", 11)

rex.dino_info()
trice.dino_info()
velo.dino_info()

rex.roar()
trice.roar()
velo.roar()

rex.eat("Meat")
trice.eat("Meat")
velo.eat("Plants")

dinosaurs = {
    "1": rex,
    "2": trice,
    "3": velo
}

print("Which dinosaur do you want information on?")
print("1 Rex (Tyrannosaurus Rex)")
print("2 Trice (Triceratops)")
print("3 Velo (Velociraptor)")
choice = input("Enter either 1, 2, or 3.")

if choice in dinosaurs:
    dino = dinosaurs[choice]
    dino.dino_info()
    dino.roar()
    
    food_choice = input("What food do you want to feed the dinosaur? ")
    dino.eat(food_choice)
else:
    print("Invalid choice!")



