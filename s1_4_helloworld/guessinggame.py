import random

highest = 10
ans = random.randint(1,highest)
print(ans)  #TODO: Remove after testing

print("Guess between 1 and {}: ".format(highest))
guess = int(input())

while guess != ans:
    if guess < ans:
        print("Incorrect. Guess higher or enter 0 to exit")
        guess = int(input())
        if guess == 0:
            break
    else:
        print("Incorrect. Guess lower or enter 0 to exit")
        guess = int(input())
        if guess == 0:
            break
if guess == 0:
    print("Quiting...")
else:
    print("You guessed right!")