# def favorite_book(title):
#     print(f"One of my favourite books is {title.title()}")
# favorite_book('the book of tomorrow')
 # def describe_pet(animal_type, pet_name):
#     """Display information about the pet"""
    # print(f"\nI have a {animal_type}.")
    # print(f"\nMy {animal_type}'s name is {pet_name.title()}")

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')
# describe_pet('cat', 'johnson')
# describe_pet('cow', 'pengus')
# describe_pet('chicken', 'melni')

# describe_pet(animal_type='hamster', pet_name='harry')
# def make_shirt(size='L', message='I love Python'):
#     print(f"The shirt with size {size} will print the message - {message}")

# make_shirt('L', 'No rapture')
# make_shirt(size='XL', message='Incase of a rapture')
# make_shirt()
# make_shirt('M', 'Prediction')
# make_shirt(message='End of times', size='XXL')

# def describe_city(name='Nairobi', country='Kenya'):
#     print(f"{name.title()} is in {country.title()}")

# describe_city()
# describe_city('Ougadougou', 'Togo')
# describe_city(name='Antananarivo', country='Madagascar')
# describe_city('Kampala', 'Uganda')
# describe_city('Reykjavik', 'Iceland')
# def get_formatted_name(first_name, last_name):
#     # the line below will return a full, neatly formatted name
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# def get_formatted_name():
#     full_name = input("Enter the first and last name: ")
#     return full_name.title()
# names = get_formatted_name()
# for i in range(5):
#     print(names)
# def get_formatted_name(first_name, middle_name, last_name):
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('john', 'lee', 'hooper')
# print(musician)
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"

#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# musician = get_formatted_name('john', 'hooper', 'lee')

# print(musician)
##########################
##Returning a Dictionary##
##########################
# def build_person(first_name, last_name, occupation, hobby, age=None):
#     person = {'first': first_name, 'last': last_name, 'hobby': hobby, 'occupation': occupation}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', 'Software Engineer', 'Basketball', age=23)
# print(musician)

# def get_formatted_name(first_name, last_name):
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello {formatted_name}! Welcome to the real world!")


# def city_country(city, country):
#     info = f'"{city}, {country}"'
#     return info
# value = city_country("Nairobi", "Kenya")
# value1 = city_country("Jordan", "Israel")
# value2 = city_country("Rio De Janeiro", "Brazil")
# print(value)
# print(value1)
# print(value2)
# def make_album(artist_name, album_title):
#     album = {'Artist': artist_name, 'Album': album_title}
#     return album
# album1 = make_album('lowki the great'.capitalize(), 'once upon a time'.capitalize())
# print(album1)
# album2 = make_album('tyler, the creator'.capitalize(), 'igor'.capitalize())
# print(album2)
# album3 = make_album('nirvana', 'nevermind')

# def make_album(artist_name, album_title):
#     album = {'Artist': artist_name, 'Album': album_title}
#     return album

# while True:
#     print("Please enter the artist's name and album name: ")
#     print("enter 'q' at any time to quit")
#     art_name = input("Artist's name: ")
#     if art_name == 'q':
#         break
#     alb_name = input("Album's name: ")
#     if alb_name == 'q':
#         break
#     formatted_name = make_album(artist_name=art_name, album_title=alb_name)

#     # print(f"{formatted_name}")
    
# musician_dict = make_album(artist_name=art_name, album_title=alb_name)
# print(musician_dict)
# def greet_users(names):
#     for name in names:
#         msg = f"Hello, {name.title()}! How are you?"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot', 'george', 'kai', 'jorge', 'eve', 'dilahunty', 'matt']
# greet_users(usernames)
#######################
#####EXPECTATIONS######
#######################
