print("---Ewok Ops: Lists & Loops ---\n")

ewoks = ["Wickets", "Paploo", "Teebo", "Nippet"]

print("First ewok", ewoks[0])
print("Last ewok", ewoks[-1])
print("Middle pair:", ewoks[1:3])
print("Roster size:", len(ewoks))

print("\n-- Updating the roster --")
ewoks.append("Chief Chirpa")
print("After append:", ewoks)

ewoks.insert(0, "Logray")
print("After insert at front", ewoks)

ewoks.extend(["Kneesaa", "Latara"])
print("After extend:", ewoks)

ewoks.remove("Paploo")
print("After remove Paploo", ewoks)

removed = ewoks.pop()
print("Popped off", removed)
print("After pop", ewoks)

ewoks.sort()
print("Sorted A-Z", ewoks)
ewoks.reverse()
print("Reversed Z-A", ewoks)

print("\n-- Roll Call --")
for ewok in ewoks:
    print("Present:", ewok)

print("\n-- Numbered roll call (enumerate) --")
for i, ewok in enumerate(ewoks, start=1):
    print(f"{i}. {ewok}")

print("\n-- L-only squad --")
for ewok in ewoks:
    if ewok.startswith("L"):
        print("L-squad members:", ewok)

print("\n-- Uppercase call signs --")
call_signs = []
for ewok in ewoks:
    call_signs.append(ewok.upper())
print(call_signs)

print("\n-- Longest Name --")
longest = ""
for ewok in ewoks:
    if len(ewok) > len(longest):
        longest = ewok
print("Longest:", longest)

print("\n=== Supply Drop ===")
items = ["Berries", "Spears", "Bandages", "Glider Parts"]
counts = [30, 12, 8, 6]

if len(items) != len(counts):
    print("Data error: items and counts are different lengths!")
else:
    total = 0
    for i in range(len(items)):
        line = f"{items[i]} x {counts[i]}"
        print(line)
        total += counts[i]
    print("Total units:", total)