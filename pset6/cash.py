from cs50 import get_float

# Input with validation
while True:
    n = get_float("Change owed: ")
    if (n > 0.0):
        break

# Convert dollars into cents

cents = round(n * 100)
count = 0

if cents >= 25:
    division = cents // 25
    cents = cents - (division * 25)
    count += division

if cents >= 10:
    division = cents // 10
    cents = cents - (division * 10)
    count += division

if cents >= 5:
    division = cents // 5
    cents = cents - (division * 5)
    count += division

if cents >= 1:
    division = cents // 1
    cents = cents - (division * 1)
    count += division

print(count)