#    ____              _______       ______                          _____ __            ___
#   / __ \(_)  _____  / / ___/____  / __/ /__      ______ _________ / ___// /___  ______/ (_)___  _____
#  / /_/ / / |/_/ _ \/ /\__ \/ __ \/ /_/ __/ | /| / / __ `/ ___/ _ \\__ \/ __/ / / / __  / / __ \/ ___/
# / ____/ />  </  __/ /___/ / /_/ / __/ /_ | |/ |/ / /_/ / /  /  __/__/ / /_/ /_/ / /_/ / / /_/ (__  )
#/_/   /_/_/|_|\___/_//____/\____/_/  \__/ |__/|__/\__,_/_/   \___/____/\__/\__,_/\__,_/_/\____/____/
#

# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# base = "<| . . . . . . . . . . |>"
# floor= "<|=====================|>"
# floor= " \/\/\/\/\/\/\/\/\/\/\/  "

import random

textris = " ___________________  ________\n/_  __/ __/_  __/ _ \/  _/ __/\n / / / _/  / / / , _// /_\ \  \n/_/ /___/ /_/ /_/|_/___/___/  \n"

base = "<| . . . . . . . . . .|>"
floor = "<|====================|>\n \/\/\/\/\/\/\/\/\/\/\/  "

# 0 represents empty
# 1 represents a moving block
# -1 represents a stationary block

clearGameRow = [0,0,0,0,0,0,0,0,0,0]

gameState = [list(clearGameRow) for _ in range(20)]

# blockState = list(gameState)

blockPosRows = [0,1]

LShape = [
	[0,0,0,0,1,1,1,0,0,0],
	[0,0,0,0,1,0,0,0,0,0]
]

LineShape = [
	[0,0,0,1,1,1,1,0,0,0]
]

SquareShape = [
	[0,0,0,0,1,1,0,0,0,0],
	[0,0,0,0,1,1,0,0,0,0]
]

TShape = [
	[0,0,0,0,1,1,1,0,0,0],
	[0,0,0,0,0,1,0,0,0,0]
]

ZLeftShape = [
	[0,0,0,0,1,1,0,0,0,0],
	[0,0,0,0,0,1,1,0,0,0]
]

ZRightShape = [
	[0,0,0,0,0,1,1,0,0,0],
	[0,0,0,0,1,1,0,0,0,0]
]

Shapes = [LShape, LineShape, SquareShape, TShape, ZLeftShape, ZRightShape]

needToSpawn = True

spawnedShape = None

gameScore = 0

def spawnShape():
	global needToSpawn
	global spawnedShape
	global blockPosRows
	# Get a random shape from the list
	spawnedShape = random.choice(Shapes)

	# Set the shape in the game state
	for i in range(0, len(spawnedShape)):
		for j in range(0, len(spawnedShape[i])):
			gameState[i][j] = spawnedShape[i][j]
	blockPosRows = [0,1]
	needToSpawn = False

def printGameState():
	for i in gameState:
		# If the row is empty, print the base
		if len(set(i)) == 1:
			print(base)
		else:
			builder = "<|"
			for j in i:
				if j == 0:
					builder += " ."
				else:
					builder += "[]"
			builder += "|>"
			print(builder)
	print(floor)

def checkForFullRows():
	global gameScore
	# Check each row
	for i in range(0, len(gameState)):
		# If the row is full
		if len(set(gameState[i])) == 1 and gameState[i][0] == -1:
			# Remove the row
			gameState.pop(i)
			# Add a new empty row
			gameState.insert(0, clearGameRow)
			# Increase the score
			gameScore += 1
			# Check for more full rows
			checkForFullRows()

# def checkForGameOver():
# 	if (-1 in gameState[0]):
# 		print("Game Over!")

# def checkForShapeCollision():
# 	for i in range(0, len(gameState)):
# 		for j in range(0, len(gameState[i])):
# 			if gameState[i][j] == 1:
# 				if i + 1 <= len(gameState) - 1:
# 					if gameState[i+1][j] == -1:
# 						return True
# 				else:
# 					return True
# 	return False

def moveShape(direction):
	if direction == "down":
		# Only check the part of the gameState where the shape is
		# Move the shape from bottom up to avoid collision issues
		for i in range(len(blockPosRows) - 1, -1, -1):
			blockRow = gameState[blockPosRows[i]]

			for j in range(0, len(blockRow)):
				# If the current cell is part of the shape
				if blockRow[j] == 1:
					# If the row below is part of the board
					if blockPosRows[i] + 1 <= len(gameState) - 1:
						# The row below
						nextBlockRow = gameState[blockPosRows[i]+1]
						# If the cell below is not empty
						if nextBlockRow[j] == -1:
							return
						nextBlockRow[j] = 1
						blockRow[j] = 0
			# After moving down the row, move the pointer down
			blockPosRows[i] += 1

		# Old way
		# # Ranges are exclusive, so we range to -1 to get to the 0th
		# for i in range(len(gameState) - 1, -1, -1):
		# 	for j in range(0, len(gameState[i])):
		# 		# If the current cell is part of the shape
		# 		if gameState[i][j] == 1:
		# 			# Move the cell down
		# 			if i + 1 <= len(gameState) - 1:
		# 				gameState[i+1][j] = 1
		# 				gameState[i][j] = 0
		# 			else:
		# 				return
	if direction == "left":
		for i in blockPosRows:
			# Check if the shape is at the left edge
			if gameState[i][0] != 0:
				return
			# Shift the row to the left
			gameState[i] = gameState[i][1:] + [0]
		# Old way
		# for i in range(0, len(gameState)):
		# 	for j in range(0, len(gameState[i])):
		# 		# If the current cell is part of the shape
		# 		if gameState[i][j] == 1:
		# 			if j - 1 < 0 or i >= len(gameState) - 2:
		# 				return
		# 			gameState[i][j] = 0
		# 			gameState[i][j-1] = 1
	if direction == "right":
		for i in blockPosRows:
			if gameState[i][-1] != 0:
				return
			# Shift the row to the right
			gameState[i] = [0] + gameState[i][:-1]

		# Old way
		# for i in range(0, len(gameState)):
		# 	for j in range(len(gameState[i]) - 1, -1, -1):
		# 		# If the current cell is part of the shape
		# 		if gameState[i][j] == 1:
		# 			# Move the cell right
		# 			if j + 1 > len(gameState[i]) - 1 or i >= len(gameState) - 2:
		# 				return
		# 			gameState[i][j+1] = 1
		# 			gameState[i][j] = 0
	if direction == "drop":
		for i in range(len(blockPosRows) - 1, -1, -1):
			blockRow = gameState[blockPosRows[i]]

			for j in range(0, len(blockRow)):
				# If the current cell is part of the shape
				if blockRow[j] == 1:
					# If the row below is part of the board
					if blockPosRows[i] + 1 <= len(gameState) - 1:
						# The row below
						nextBlockRow = gameState[blockPosRows[i]+1]
						# If the cell below is not empty
						if nextBlockRow[j] == -1:
							return
						nextBlockRow[j] = 1
						blockRow[j] = 0
			# After moving down the row, move the pointer down
			blockPosRows[i] += 1
		# rows = []
		# for i in range(0, len(gameState)):
		# 	if gameState[i].count(1) > 0:
		# 		rows.append(i)
	
		# for i in rows:
		# 	gameState[i] = list(clearGameRow)

		# for i in range(0, len(spawnedShape)):
		# 	for j in range(0, len(spawnedShape[i])):
		# 		gameState[i - 2 + len(gameState)][j] = spawnedShape[i][j]
		
		# Old way 
		# for i in range(len(gameState) - 1, -1, -1):
		# 	for j in range(0, len(gameState[i])):
		# 		# If the current cell is part of the shape
		# 		if gameState[i][j] == 1:
		# 			# Move the cell down
		# 			# if i + 1 <= len(gameState) - 1:
		# 			gameState[len(gameState) - 1][j] = -1
		# 			gameState[i][j] = 0
		# 			# else:
					# 	return
		# for i in range(len(gameState) - 1, -1, -1):
		# 	for j in range(0, len(gameState[i])):
		# 		# If the current cell is part of the shape
		# 		if gameState[i][j] == 1:
		# 			if (i < len(gameState) - 2):
		# 				gameState[len(gameState) - 1][j] = -1
		# 				gameState[i][j] = 0
		# 			else:
		# 				return

def main():
	try:
		print(textris)
		print("Controls: left (l), right (r), drop (d)\n")
		while True:
			if needToSpawn:
				spawnShape()

			printGameState()
			print("Score:", gameScore)
			move = input("Your move: ").lower()
			if move in ["left", "l"]:
				moveShape("left")
			elif move in ["right", "r"]:
				moveShape("right")
			elif move in ["drop", "d"]:
				moveShape("drop")
			moveShape("down")
	except KeyboardInterrupt:
		print("\nExiting...")
main()