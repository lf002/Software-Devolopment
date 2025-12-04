class Character:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number


class Hero(Character):
    def __init__(self, name, id_number, level, loot):
        super().__init__(name, id_number)
        self.level = level
        self.loot = loot  


class Boss(Character):
    def __init__(self, name, id_number, level, hp, attack_damage):
        super().__init__(name, id_number)
        self.level = level
        self.hp = hp
        self.attack_damage = attack_damage

    def lifespan(self):
    
        return self.hp / 1000