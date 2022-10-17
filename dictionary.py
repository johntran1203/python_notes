instructor = {
    'name': 'colt',
    'ouwn_dogs': True,
    'favorite_number': 2,
    'favorire_language': 'Python',
    'is_funny': False,
}

# for value in instructor.values():
#     print(value)

# for k,y in instructor.items():
#     print(k,y)

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donation = 0

for value in donations.values():
    total_donation += value

# print(total_donation)

# if 'colt' in instructor.values():
#     print (True)

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')

playlist = {
    'title': 'patgaonia bus',
    'author': 'colt steele',
    'songs': [
        {'title': 'song1', 'artist': ['blue'], 'duraiton': 2.5},
        {'title': 'song2', 'artist': ['kitty'], 'duraiton': 5.25},
        {'title': 'meowmewo', 'artist': ['garfield'], 'duraiton': 2.},

    ]
}

for sing in playlist['songs']:
    print(sing['title'])