products = [
    # Brand, Model, Qty, Price
    ['apple', 'iPhone 13', 25, 5000],
    ['Samsung', 'S20', 18, 4000],
    ['Huwaei', 'P20', 5, 3000],
    ['Sony', 'Xperia Z', 4, 3500]
]

newProduct = ['Nokia', '3310', 5, 1000]
# Add your code below

# (1) Add the new product to 'products'
products.append(['Nokia', '3210', 100, 500])

# (2) Change the price of 'iPhone 13' to 4500
products[0][3] = 9999

# (3) Print the number of 'iPhone 13' products
print(products[0][2])

# (4) Change the quantity of 'S20' to 20
products[1][2] += 2

# (5) Correct the name 'apple' to 'Apple'
products[0][0] = "Apple"

print(products)