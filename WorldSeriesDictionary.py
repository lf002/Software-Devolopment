with open("WorldSeriesWinners.txt", "r") as f:
    winners_list = [line.strip() for line in f if line.strip()]

Teams = {}
for team in winners_list:
    Teams[team] = Teams.get(team, 0) + 1

Years = {}
start_year = 1903
for i, team in enumerate(winners_list):
    year = start_year + i
    Years[year] = team

year_input = int(input("Enter a year between 1903 and 2021: "))

if year_input in [1904, 1994]:
    print("The World Series did not have a winner in", year_input)
elif year_input < 1903 or year_input > 2021:
    print("Year not in range.")
else:
    winner = Years[year_input]
    print("Winner in", year_input, ":", winner)
    print("Total championships:", Teams[winner])