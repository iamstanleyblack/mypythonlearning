prompt = "\nWelcome to the movie ticket booking system"
prompt += "\nEnter your age to generate a prompt for your ticket charge"
prompt += "\n: "

age = int(input(prompt))
active = True
while active:
    if age <= 3:
        print("\nWelcome to the movies! The ticket is free! Enjoy the movies!")
        break
    elif age >= 3 and age <= 12:
        print("\n Welcome to the movies! The ticket will cost $10. Enjoy the show")
        break
    else:
        print("\nWelcome to the movies! The ticket will cost you $15. Enjoy the show")
        break
    