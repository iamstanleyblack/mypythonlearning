sandwich_orders = ['egg sandwich', 'pineapple sandwich', 'apple pie sandwich', 'jack fruit sandwich', 'soup sandwich', 'salad sandwich', 'mustard sandwich']
finished_sandwiches = []

for each_sandwich in sandwich_orders:
    print(f"I made your {each_sandwich}")
    finished_sandwiches.append(each_sandwich)
print("\n")
print("These are all the sandwiches that I made: ")
for all_sandwiches in finished_sandwiches:
    print(f"-{all_sandwiches}")