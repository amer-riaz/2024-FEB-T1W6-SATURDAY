# is_raining = False
is_raining = input("Is it raining? Yes or No? ")

# if is_raining:
#     print("I need an umbrella")
# else:
#     print("I don't need an umbrella")

# Ternary operator
# <statement to execute when true> if <condition> else <statement to execute when false>

print("I need an umbrella") if is_raining == "Yes" else print("I don't need an umbrella")

# truthy - condition - falsy    python ternary operator
# condition - truthy - falsy    Javascript ternary operator