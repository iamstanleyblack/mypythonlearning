cars = ['subaru', 'atenza', 'mercedes', 'lamborgini', 'subaru', 'ferrari', 'subaru']

print(cars)

while 'subaru' in cars:
    cars.remove('subaru')

print(f"We have now removed duplicate car here")
print(cars)