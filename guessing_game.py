import random
count = 5
ans = 'yes' or 'y'
win = False

print("Guess what number the computer has generated between 1 - 50")

print("You have 5 chances left")
print("---------------------------------")
while ans == 'yes' or 'y':
    randomNumber = random.randint(1, 50)
    print("Guesses Remaining : ", count)
    guess = int(input("Enter your answer : "))
    if randomNumber == guess:
        print("Congratulations! YOu have guessed it right)")
        win = True
    else:
        print("Wrong!")
        count = count - 1
        if count == 0:
            print("Oops, Sorry! You are out of chances")
            print("The guess was : ",randomNumber)
    if win == True or count == 0:
        ans = input("Wanna play again? ")
        if ans == 'yes' or 'y':
            count == 5
            win = False