sandwich_orders = ['egg sandwich', 'pastrami', 'pineapple sandwich', 'apple pie sandwich', 'pastrami', 'jack fruit sandwich', 'soup sandwich', 'pastrami', 'salad sandwich', 'mustard sandwich', 'pastrami']
print("Our apologies dear Customer! The Deli has run out of pastrami")
finished_sandwiches = []
print("Before noon, we had:")
for sandwiches_we_had in sandwich_orders:
    print(f"\t-{sandwiches_we_had}")
pastrami_present = True
while 'pastrami' in sandwich_orders:
    if pastrami_present:
        sandwich_orders.remove('pastrami')
    else:
        pastrami_present = False
print("These are the sandwiches we currently have")
for each_sandwich in sandwich_orders:
    finished_sandwiches.append(each_sandwich)
    print(f"{each_sandwich} is available")
        

