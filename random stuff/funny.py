# -----------------------------
# Imports
# -----------------------------
import random
import time

# -----------------------------
# Welcome / Title Screen
# -----------------------------
width = 80
print("\n" * 2)
print("🎉 WELCOME TO 'THE OFFICE SURVIVAL QUEST!' 🎉".center(width))
print("Survive the workday with your energy, coffee, and wits.".center(width))
print("Can you make it to the end without crashing?".center(width))
print("\n" * 1)
input("Press Enter to start your adventure...")

# -----------------------------
# Player Stats
# -----------------------------

# This is where the energy of the player is deducted or increased based on there answers and decisions.
# -----------------------------
energy = 10
inventory = []

def check_status():
    """Prints current energy and inventory"""
    print(f"\nEnergy: {energy} | Inventory: {inventory}\n")

# -----------------------------
# Mini-Quiz Function
# -----------------------------

# This is where the person answers the questions when they select the first choice "1"
# -----------------------------
def mini_quiz():
    """Ask all quiz questions one by one"""
    global energy
    quizzes = [
        {"question": "What is 2 * 4?", "answer": "8", "energy_gain": 4},
        {"question": "What animal meows?", "answer": "cat", "energy_gain": 3},
        {"question": "Largest planet in our solar system?", "answer": "jupiter", "energy_gain": 5},
        {"question": "What animal barks?", "answer": "dog", "energy_gain": 2}
    ]

    # Loop through all questions
    for quiz in quizzes:
        print("\n" + quiz["question"])
        answer = input("> ").strip().lower()
        
        # Normalize answer and check
        if answer == quiz["answer"].lower():
            energy += quiz["energy_gain"]
            print(f"✅ Correct! Energy +{quiz['energy_gain']}")
        else:
            energy -= 2
            print("❌ Wrong! Energy -2")

# -----------------------------
# Drink Coffee Function
# -----------------------------
def drink_coffee():
    global energy
    if "Coffee" in inventory:
        inventory.remove("Coffee")
        energy += 5
        print("☕ You drink a cup of coffee. Energy +5!")
    else:
        print("No coffee in inventory! Find some first.")

# -----------------------------
# Random Office Events
# -----------------------------
def random_event():
    global energy
    events = [
        "You slip on a banana peel. Energy -1",
        "You find a hidden stash of snacks! Energy +3",
        "Printer explodes! Chaos ensues. Energy -4",
        "You send a funny meme to Slack. Coworkers laugh. Energy +2",
        "You accidentally reply-all to an email. Energy -3"
    ]
    event = random.choice(events)
    print("\n" + event)
    if "Energy +" in event:
        energy += int(event.split("Energy +")[1])
    elif "Energy -" in event:
        energy -= int(event.split("Energy -")[1])

# -----------------------------
# Main Game Loop
# -----------------------------
while True:
    # Check win/lose conditions
    if energy <= 0:
        print("\n💀 You ran out of energy! Game Over!")
        break
    elif energy >= 30:
        print("\n🏆 You survived the workday like a legend! Congrats!")
        break

    # Show status
    check_status()

    # Player choices
    print("Where would you like to go?")
    print("1. Your Desk (mini-quiz)")
    print("2. Break Room (find coffee or snack)")
    print("3. Hallway (random event)")
    print("4. Drink Coffee")
    print("5. Quit Game")

    choice = input("> ").strip()

    if choice == "1":
        print("\n🖥️ You sit at your desk and focus...")
        mini_quiz()  # now asks all questions and subtracts energy correctly
    elif choice == "2":
        find = random.choice(["Coffee", "Cookie", "Nothing"])
        if find == "Nothing":
            print("\nNothing useful here. Just stale air.")
        else:
            inventory.append(find)
            print(f"\nYou found {find}! Added to inventory.")
    elif choice == "3":
        print("\n🚶 Walking the office hallway...")
        random_event()
    elif choice == "4":
        drink_coffee()
    elif choice == "5":
        print("\n👋 You quit the game. Goodbye!")
        break
    else:
        print("\n❌ Invalid choice. Try again.")

    time.sleep(1)