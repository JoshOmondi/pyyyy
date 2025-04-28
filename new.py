# Create an empty list for storing squares
squareList = []

# Define intList (you can replace this with any list of integers)
intList = [1, 2, 3, 4, 5]  # Example list

# Loop through intList, square every item, and append to squareList
for x in intList:
    squareList.append(pow(x, 2))

# Print the list of squared values
print(squareList)
