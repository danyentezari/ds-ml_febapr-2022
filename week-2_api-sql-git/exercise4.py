# (1) Create a function called coffeeMachine

# (2) Give this function four parameters: 
# 'coffeeOption', 'sizeOption', 'milkOption', 'sugarOption'

# (3) Create inside this a function an empty List called 'theOrder' 

# (4) The function will append to 'theOrder' the arguments of all four parameters

# (5) The function must return the 'theOrder'. For example,
# theOrder = ['Latte', 'Skimmed Milk', 'Medium', 'White Sugar']

# (6) Use input() to ask the user for all three arguments
# for example, input("Please enter coffee option:")

# (7) Pass these arguments to the function AFTER calling it
# for example, coffeeMachine("Americano", "Coconut Milk", "Large", "No Sugar")


def coffeeMachine(coffeeOption, sizeOption, milkOption, sugarOption):
    theOrder = []

    theOrder.append(coffeeOption)
    theOrder.append(sizeOption)
    theOrder.append(milkOption)
    theOrder.append(sugarOption)

    return theOrder



print(
    coffeeMachine(
        input("Please enter coffee option: "),
        input("Please choose the size: "),
        input("Please choose milk option: "),
        input("Please choose sugar option: ")
    )
)