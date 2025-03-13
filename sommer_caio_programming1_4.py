#
# Caio Sommer, 06/02/2025
#

# n is the secret number
n = 4
while True:
    # try/except value error makes the program not crash if the user enters a character instead of an integer
    try:
        g = int(input("Guess your first number: "))
        break
    except ValueError:
        pass
# no if statement needed, but I'd put one here saying:
# if g != n
while g != n:
    g = int(input("Incorrect, guess again: "))

print("Correct, well done!")

n = 7
# Better if there are multiple conditions that the loop has to check for
while True:
    try:
        g = int(input("Guess a secret number: "))
    except ValueError:
        pass
    if g == n:
        print("Congratulations, you found the secret number!")
        break
    g = int(input("Guess a secret number: "))

# I don't have a preference for any type when the 
# conditions are simple like this, but if an event
# is needed (for example a socket message or exception)
# I'd use while True: with break.