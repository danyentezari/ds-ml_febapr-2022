from math import prod
from numpy import product


products = [
    # Brand, Model, Qty, Price 
    ['apple','iPhone 13', 25, 5000],
    ['Samsung','S20', 18, 4000],
    ['Huwaei','P20', 5, 3000],
    ['Sony','Xperia Z', 4, 3500]
]


newProduct = ['Nokia','3310', 5, 1000]
# Add your code below

# (1) Add the new product to 'products'
products.append(newProduct)

# (2) Change the price of 'iPhone 13' to 4500
products[0][3] = 4500

# (3) Print the number of 'iPhone 13' products
products[0][2]

# (4) Change the quantity of 'S20' to 20
products[1][2] = 20

# (5) Correct the name 'apple' to 'Apple'
products[0][0] = "Apple"


# (Bonus) Add up all of the quantities of the products
# Solution 1
totalQty = 0

for index, value in enumerate(products):
    totalQty = totalQty + products[index][2]

print(totalQty)



# Solution 2
totalQty = 0

for index in range(0, len(products)):
    totalQty = totalQty + products[index][2]

print(totalQty)