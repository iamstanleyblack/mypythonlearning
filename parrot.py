'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number +=1
'''

# prompt = "\nTell me something, and I will repeat it back to you "
# prompt += "\nEnter 'quit' to end the program"
# prompt += "\n: "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# prompt = "\nTell me something, and I will repeat it back to you "
# prompt += "\nEnter 'quit' to end the program"
# prompt += "\n: "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have been to"
# prompt += "\nEnter 'quit' to end the program"
# prompt += "\n: "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to the {city.title()}!")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(f"The current number is {current_number}")
