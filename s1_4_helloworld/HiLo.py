low = 1
high = 1000

print("Please think of a number between {} and {}: ".format(low, high))
input("Press Enter to start")

guesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":
        #guess higher
        pass
    elif high_low == "l":
        #guess lower
        pass
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h,l or c")

    guesses = guesses + 1
    