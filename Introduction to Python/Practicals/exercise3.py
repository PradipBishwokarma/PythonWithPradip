'''
Working with number variables:
You're building a recipe scaler to adjust ingredient quantities for different party sizes. Your base recipe for pasta sauce serves 4 people and requires certain amounts of ingredients. Some ingredients come in whole units, while others need decimal measurements. You need to store these quantities using the appropriate data types so your recipe scaler can perform calculations accurately later.
'''

'''
Instructions:
Store the number of garlic cloves (3) as an integer variable called garlic_cloves.
Store the amount of olive oil in tablespoons (2.5) as a float variable called olive_oil_tbsp.
Increase the amount of olive oil by 1 tablespoon and store it to new_olive_oil_tbsp.
'''

# Store the number of garlic cloves as an integer
garlic_cloves = 3

# Store the olive oil amount as a float
olive_oil_tbsp = 2.5
print(olive_oil_tbsp)

# Increase the olive oil amount
new_olive_oil_tbsp = 2.5 + 1

print(garlic_cloves)
print(new_olive_oil_tbsp)


'''
Working with booleans:
As you build your recipe scaler project, you need to track which ingredients you already have at home versus which ones you need to buy at the store. Booleans are perfect for storing this yes/no information. You've already created variables for some ingredients in your recipe, and now you'll add boolean variables to track their availability.
'''

'''
Instructions:
Create a boolean variable called has_pasta and set it to True to indicate you already have pasta at home.
Create a boolean variable called has_garlic and set it to False to indicate you need to buy garlic.
'''

# Track if you have pasta at home
has_pasta = True

# Track if you have garlic
has_garlic = False

print(has_pasta)
print(has_garlic)


'''
Checking data types:
As you build your recipe scaler project, you've started storing different types of ingredient information in variables. You have the number of garlic cloves as a whole number, the amount of olive oil as a decimal, and whether you need to shop for pasta or garlic as a yes/no value. Before you continue building your scaler, it's important to verify a variable is storing the correct data type. Python's type() function will help you check this. The variables olive_oil_tbsp and has_pasta have been loaded for you.
'''

'''
Instructions:
Print the data type of the olive_oil_tbsp variable.
Print the data type of the has_pasta variable.
'''

# Check the data type of olive_oil_tbsp
print(type(olive_oil_tbsp))

# Check the data type of has_pasta
print(type(has_pasta))