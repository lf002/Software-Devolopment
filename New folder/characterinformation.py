from characters import Hero, Boss

hero_name = input("Enter Hero name: ")
hero_id = int(input("Enter Hero ID: "))
hero_level = int(input("Enter Hero level (1-5): "))
hero_loot = float(input("Enter Hero loot (xx.xx): "))

hero = Hero(hero_name, hero_id, hero_level, hero_loot)

boss_name = input("Enter Boss name: ")
boss_id = int(input("Enter Boss ID: "))
boss_level = int(input("Enter Boss level (1-5): "))
boss_hp = int(input("Enter Boss HP: "))
boss_attack = int(input("Enter Boss attack damage: "))

boss = Boss(boss_name, boss_id, boss_level, boss_hp, boss_attack)

print("\n--- HERO INFORMATION ---")
print("Name:", hero.name)
print("ID Number:", hero.id_number)
print("Level:", hero.level)
print("Loot: {:.2f}".format(hero.loot))

print("\n--- BOSS INFORMATION ---")
print("Name:", boss.name)
print("ID Number:", boss.id_number)
print("Level:", boss.level)
print("HP:", boss.hp)
print("Attack Damage:", boss.attack_damage)
print("Lifespan:", boss.lifespan())