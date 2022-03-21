# (1) Built-in Functions
# ---------------------------------------------------------
# print("Hello there!")

# userName = input("Please enter your name: ")
# print("Name is", userName)


# (2) Variables
# ---------------------------------------------------------
# 1 - Always start with lowercase letter
# 2 - Do not name after reserved keyword or python code
# 3 - Use camel case or underscore convention

# no convention
# firstname = "Mohammad"

# underscore convention
# first_name = "Ahmad"

# camel case convention
# firstName = "Karan"

# myfavoriterestaurantindubai = "Eat Greek"
# my_favorite_restaurant_in_dubai = "Eat Greek"
# myFavoriteRestaurantInDubai = "Eat Greek"


# print("This is one line\nthis is another")


# (3) Operators
# ---------------------------------------------------------
# =                      Assignment
# ==                     Comparison
# <                      Less than comparison
# >                      Greater than comparison
# <=                     Less than or equal
# >=                     Greater than or equal
# !=                     Not equal
# !                      Not
# not
# and
# or
# %                      Modulo



# (4) Control Statements
# ---------------------------------------------------------
# if/else
# for loop
# while loop


# price = 500
# budget = 500

# if price <= budget:
#     print("Buy the product")
# else:
#     print("Don't buy the product")



# Model S, CLS500, Mustang
# customerSelection = "CLS500"

# if customerSelection == "Model S":
#     print("Tesla")
# elif customerSelection == "CLS500":
#     print("Mercedez Bens")
# elif customerSelection == "Mustang":
#     print("Ford")
# else:
#     print("Not available. Please try again")

# passengerClass = "Business"

# if passengerClass == "First":
#     print(1)
# elif passengerClass == "Business":
#     print(2)
# elif passengerClass == "Economy":
#     print(3)
# else:
#     print(0)



# airline = input("Enter airline name: ")

# if airline == "Emirates" or airline == "Qantas":
#     print("Terminal 3")

# elif airline == "FlyDubai":
#     print("Terminal 2")

# elif airline == "Qatar Airways":
#     print("Terminal 1")

# else:
#     print("No info available")


# ticket = True
# booster = True

# if ticket == True and booster == True:  
#     print("You may enter")
# else:
#     print("You may not enter")


# cities = ['Dubai','London','Dublin','Amman','Tokyo','Berlin']

# for index in range(0, len(cities)):
#     print( cities[index] )


# departure_destination = [
#     'London',
#     'Dublin',
#     'Amman',
#     'Tokyo',
#     'Berlin',
#     'Riyadh'
# ]

# for value in cities:
#     print( value )


# for index, value in enumerate(departure_destination):
#     if value == 'Riyadh':
#         print( 'Riyadh flight order:', index+1, 'out of', len(departure_destination)  )


# print( cities[0] )
# print( cities[1] )
# print( cities[2] )
# print( cities[3] )
# print( cities[4] )



# for index, value in enumerate(cities):
#     print(value, index)


# print( cities[0] )
# print( cities[1] )
# print( cities[2] )
# print( cities[3] )
# print( cities[4] )







# (5) Data Structure: List
# ---------------------------------------------------------
airlines = [
    "British Airways",          # 0
    "Emirates",                 # 1
    "Fly Dubai",                # 2
    "KLM",                      # 3
    "Qantas",                   # 4
    "Qatar Airways"             # 5
]

# Accessing a specific element
# print( airlines[2] )
# print( airlines[5] )

# Count the elements of a List
# print( len(airlines) )

# Reassign value of an element
# airlines[5] = 'Malaysian Airlines'



# List Methods:
# https://www.w3schools.com/python/python_ref_list.asp
# .append(value)                     Add element to end of List
# .pop(index)                        Removes element from end (or specific position) of List
# .insert(index, value)              Add element specific position of List
# .remove(index)                     Removes element with value

# airlines.append('Singapore Airlines')
# print(airlines)

# airlines.pop()
# print(airlines)

# airlines.pop(3)
# print(airlines)



# List with Mixed Data Types

# Example 1
# customerData = [
#     'John',
#     'Doe',
#     True,
#     ['050 1234567','john@email.com'],
#     7
# ]
# print( customerData[3][0] )


# Example 2
# countries = [
#     ['UAE','Abu Dhabi','Abu Dhabi International'],
#     ['Japan','Tokyo','Hanida International'],
#     ['France','Paris','Charles de Gaul']
# ]
# print( countries[1][2] )





# Lists
# Mutable
# Methods: 
# https://www.w3schools.com/python/python_ref_list.asp
customers = [
    'Mohammad',
    'Mohammad',
    'Mary',
    'Mike'
]

# Tuples
# Immutable
# Methods:
# https://www.w3schools.com/python/python_ref_tuple.asp
citiesUAE = (
    'Abu Dhabi',
    'Dubai',
    'Sharjah',
    'Ras Al Khaimah',
    'Umm Al Quwain',
    'Fujairah'
)

# Example 1
# print(citiesUAE[2])


# Sets
# Mutable
# Unique
# Methods:
# https://www.w3schools.com/python/python_ref_set.asp
days = {'Mon','Tue','Wed','Thu','Fr','Sat','Sun'}


# Dictionaries
# Keys must be entered and be unique
# Mutable
# Methods:
# https://www.w3schools.com/python/python_ref_dictionary.asp

# Example 1
countries = {
    'UAE': 'Abu Dhabi',
    'UK': 'London',
    'Japan': 'Tokyo',
    'China': 'Beijing',
    'Jordan': 'Amman'
}
# print(countries['UAE'])


# Example 2
employees2 = {
    'ceo': 'Karan',
    'coo': 'Firas',
    'consultant': 'Alshayma',
    'cco': 'Amr',
    'data scientist': 'Igor'
}



# (9) Functions
# ---------------------------------------------------------
# def sum(numA, numB):
#     result = numA + numB
#     return result

# print( sum(5,5) )
# print( sum(7,7) )
# print( sum(9,9) )

# def findPrice(modelParam):

#     products = {
#         'iPhone13': [25, 5000],
#         'S20': [18, 4000],
#         'Xperia Z': [4, 3500]
#     }

#     return products[modelParam][1]



# def findPrice(nameOfProduct):
#     products = {
#         'iPhone13': [25, 5000],
#         'S20': [18, 4000],
#         'Xperia Z': [4, 3500]
#     }
#   return products[nameOfProduct][1]


def registerUser():
    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")
    email = input("What is your email address? ")
    phoneNumber = input("What is your phone number? ")

    print("Thank you for registering.")
    print("First name: ", firstName)
    print("Last name: ", lastName)
    print("Email address: ", email)
    print("Phone number: ", phoneNumber)

    return [ firstName, lastName, email, phoneNumber ]

print( registerUser() )



# (10) Strings
# ---------------------------------------------------------
# \n            New line
# \t            Tab
# \s            Space
# \d            Digit
# \w            Alphanumeric character
