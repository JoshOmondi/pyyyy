def square_me(x):
    return x * x

# Define intList with some sample integers
intList = [1, 2, 3, 4, 5]  # Example list of integers

# Use map to apply the square_me function to each element of intList
squareList = list(map(square_me, intList))

# Print the list of squared values
print(squareList)
