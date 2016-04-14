# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20×20 grid?

gridSize = 20

# We need to cache the known grid answers in a 2D array, otherwise
# the answer takes far, far too long to return.
answers = [[0 for x in range(gridSize + 1)] for x in range(gridSize + 1)]

def traverseGrid(x,y):
	if x == y == gridSize:
		return 1

	answer = answers[x][y]
	if answers[x][y] != 0:
		return answer

	total = 0

	if x < gridSize:
		total = total + traverseGrid(x+1,y)

	if y < gridSize:
		total = total + traverseGrid(x,y+1)

	answers[x][y] = total

	return total


def traverse():
	return traverseGrid(0,0)

print(traverse())

