print("--------------------------------------")
print("----Multiple of ten or not------------")
print("--------------------------------------")
is_it_a_multiple = int(input("Enter a number and we'll see if it is a multiple of 10 or 10: "))

if is_it_a_multiple % 10 == 0:
    print(f"{is_it_a_multiple} is a multiple of 10")

else:
    print(f"{is_it_a_multiple} is not a multiple of 10")