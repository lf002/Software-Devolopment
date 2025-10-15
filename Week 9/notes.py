# This is a blueprint for all players in our game.
class Player:
    # Create a constructor to build the object from the class.
    def __init__(self, name, level):
        # These are attributes. They belong to the specific player being created.
        self.name = name
        self.health = 100
        self.level = level
        self.inventory = []  # start with an empty inventory

    # Take damage method
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage! Current health: {self.health}")

    # Another Method 
    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100  # limits over health and reduces it to 100
        print(f"{self.name} heals for {amount}! Current health: {self.health}")


# Create two separate Player Objects from Our Blueprint Above.
player1 = Player("Ninjafiveo", 100)
player2 = Player("William", 3)
enemy1 = Player("Thunderous Orc", 5)

# Each object has its OWN Data
print(f"{player1.name} is level {player1.level}, has {player1.health}.")
print(f"{player2.name} is level {player2.level}, has {player2.health}.")
player1.level = 500
print(f"{player1.name} is level {player1.level}, has {player1.health}.")

player2.take_damage(41)
print(f"{player2.name} is level {player2.level}, has {player2.health}.")
player2.heal(50)