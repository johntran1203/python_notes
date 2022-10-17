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

if 'colt' in instructor.values():
    print (True)