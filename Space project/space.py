weight = float(input("Please Enter Your Weight: "))

planets = {
    "mercury": 0.90,
    "venus": 0.91,
    "mars": 0.38,
    "jupiter": 2.34,
    "saturn": 1.06,
    "uranus": 0.92,
    "neptune": 1.19,
    "pluto": 0.063
}

for planet, factor in planets.items():
    planet_weight = round(weight * factor, 2)
    print(f"Your weight on {planet} is {planet_weight}")

print("Have a good day")







