prompt = "\nEnter all the pizza toppings you would like to have on your pizza."
prompt += "\nEnter 'quit' when you are done"
prompt += "\n: "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
