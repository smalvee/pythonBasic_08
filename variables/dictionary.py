# this is list
# student2 = ['Smith', 'smith@gmail.com', '09876543', 'Chittagong']


# this is simple dictionary
car = {
    'make': 'BMW',
    'model': 'bw22',
    'year': 2022
}


# Nested dictionary
user = {
    'name': 'smith',
    'age': '30',
    'address':
        {
            'present_address':
                {
                    'road': '01',
                    'house': '002'
                },
            'permanent_address': 'CTG'
        }
}

#
# print(car['model'])
# print(user['address'])
# print(user['address']['present_address'])
# print(user['address']['present_address']['road'])
# print(car.values())


person = {
    'name':
        {
            'first_name': 'john',
            'last_name': 'Smith'
        },
    'address':
        {
            'city': 'dhaka'
        },
    'Age': 30
}
print(person['address']['city'])


favorite_color = {
    'smith': 'red',
    'kavin': 'blue',
    'david': 'green'
}

# print(favorite_color)

# for key, value in favorite_color.items():
#     print(key, 's favorit color is', value)

for name, color in favorite_color.items():
    print(f"{name.title()}'s favorite color is {color.title()}.")
