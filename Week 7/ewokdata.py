ewok_data = {
    "name": "Wicket",
    "age": 67,
    "weapon": "Sword",
    "rank": "Warrior",
}

print("Ewok Name:", ewok_data["name"])
print("Ewok Age:", ewok_data["age"])
print("Ewok Weapon:", ewok_data["weapon"])
print("Ewok Rank:", ewok_data["rank"])

ewok_data["weapon"] = "Bow and Poison Arrow"   
ewok_data["rank"] = "Chief"           
ewok_data["homeworld"] = "Neptune"  

print("\nUpdated Ewok Data:")
for key, value in ewok_data.items():
    print(f"{key}: {value}")


ewok_tribe = {
    "Wicket": ewok_data,
    "Chief Chirpa": {
        "name": "Chief Chirpa",
        "age": 120,
        "weapon": "Staff",
        "rank": "Chief",
        "homeworld": "Endor"
    }
}

print("\nEwok Tribe Data:")
for ewok_name, ewok_info in ewok_tribe.items():
    print(f"\nEwok: {ewok_name}")
    for key, value in ewok_info.items():
        print(f"{key}: {value}")