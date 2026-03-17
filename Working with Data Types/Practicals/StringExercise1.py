'''
Multi-line strings:
Your recipe scaler project needs to store detailed cooking instructions for each recipe. These instructions often span multiple lines and include several steps. You'll practice storing a multi-line string that contains the complete cooking directions for a pasta dish, making it easy to read and maintain in your code.
'''

'''
Instructions:
Create a multi-line string variable called cooking_instructions that contains the three-step pasta cooking process shown in the comments.
'''

# Store the multi-line cooking instructions
# Step 1: Boil water in a large pot
# Step 2: Add pasta and cook for 10 minutes
# Step 3: Drain and serve with sauce
cooking_instructions = """"
 Step 1: Boil water in a large pot
 Step 2: Add pasta and cook for 10 minutes
 Step 3: Drain and serve with sauce

"""

print(cooking_instructions)


'''
Modifying string values:
Your recipe scaler project needs to handle ingredient names that users might enter in different formats. You want to update any generic entries to make your recipe clearer. Additionally, to ensure your shopping list doesn't have duplicate entries, you need to standardize all ingredient names to lowercase.
'''

'''
Instructions:
Use the .replace() method to update pasta_type by changing "pasta" to "fusilli pasta".
Convert the ingredient_one variable to lowercase using the .lower() method.
'''

pasta_type = "pasta"

# Update pasta type to be more specific
pasta_type = pasta_type.replace("pasta", "fusilli pasta")

ingredient_one = "BASIL"

# Standardize ingredient_one to lowercase
ingredient_one = ingredient_one.lower()

print(pasta_type)
print(ingredient_one)