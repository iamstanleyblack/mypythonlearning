print("---------------------------")
print("#######DREAM VACATION######")
print("---------------------------")

vacation_destinations = {}

still_answering = True
while still_answering:
    name = input("How should we call you? ")
    destination = input("Where would you like to go for vacation? ")
    vacation_destinations[name] = destination

    i_want_to_continue = input("Would you like to continue? (y/n) ")
    if i_want_to_continue == 'n':
        still_answering = False

print("--------------------")
print("####POLL RESULTS####")
print("--------------------")
for name, destination in vacation_destinations.items():
    print(f"{name.title()} would like to go to {destination}")