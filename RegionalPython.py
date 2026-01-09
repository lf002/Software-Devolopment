# Freyn, Lucas

players = int(input("How many players are participating, must be between 1 and 4"))
if 1 <= players <= 4:
 print(f"Continue,")
else:
 print("Error. The number must be through 1 and 4.")


print("Now enter all of the names of the people that are participating")

def club():
  members = []
  done = False
  while done != True:
    mem = input("Enter a name, enter 'done' when finished: ")
    if mem == "done":
      done = True 
    else:
      members.append(mem)
    print(members)
club()

# Asking the user for scores 

hole_scores = [Hole_1, Hole_2, Hole_3, Hole_4, Hole_5, Hole_6, Hole_7 , Hole_8, Hole_9] = [0, 1, 2, 3, 4, 5 , 6, 7 , 8, 9]
for i in range (1, 10):
  score = int(input("Enter score for Hole (i): "))
  



