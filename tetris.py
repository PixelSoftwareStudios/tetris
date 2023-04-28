#    ____              _______       ______                          _____ __            ___
#   / __ \(_)  _____  / / ___/____  / __/ /__      ______ _________ / ___// /___  ______/ (_)___  _____
#  / /_/ / / |/_/ _ \/ /\__ \/ __ \/ /_/ __/ | /| / / __ `/ ___/ _ \\__ \/ __/ / / / __  / / __ \/ ___/
# / ____/ />  </  __/ /___/ / /_/ / __/ /_ | |/ |/ / /_/ / /  /  __/__/ / /_/ /_/ / /_/ / / /_/ (__  )
#/_/   /_/_/|_|\___/_//____/\____/_/  \__/ |__/|__/\__,_/_/   \___/____/\__/\__,_/\__,_/_/\____/____/
#
# Started: 04/21/2023

#####
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# base = "<| . . . . . . . . . .|>"
# floor= "<|====================|>"
# floor= " \/\/\/\/\/\/\/\/\/\/\/  "
#####

import random

textris = " ___________________  ________\n/_  __/ __/_  __/ _ \/  _/ __/\n / / / _/  / / / , _// /_\ \  \n/_/ /___/ /_/ /_/|_/___/___/  \n"

# TODO: Use * operator to allow for variable game sizes
base = "<| . . . . . . . . . .|>"
floor = "<|====================|>\n \/\/\/\/\/\/\/\/\/\/\/  "

# TODO: Refactor to use a list comprehension to allow for variable game sizes
clearGameRow = [0,0,0,0,0,0,0,0,0,0]

gameState = [list(clearGameRow) for _ in range(20)]

# Track the position of the current block
blockPosRows = [[], []]

needToSpawn = True

gameScore = 0

# 0 represents empty
# 1 represents a moving block
# -1 represents a stationary block

# Gameplay TODOS:
# TODO: Check for block collision
# TODO: Check for full row, remove row, move down blocks on top, and increment score
# TODO: Check for game over
# TODO: Implement block rotation

# Possible block shapes
IBlock = {
	"shape": [
		[0,0,0,1,1,1,1,0,0,0]
	],
	"startPos": [
		[3, 0], [6, 0]
	]
}

LBlock = {
	"shape": [
		[0,0,0,0,1,1,1,0,0,0],
		[0,0,0,0,1,0,0,0,0,0]
	],
	"startPos": [
		[4, 0], [6, 1]
	]
}

# rip von
OBlock = {
	"shape": [
		[0,0,0,0,1,1,0,0,0,0],
		[0,0,0,0,1,1,0,0,0,0]
	],
	"startPos": [
		[4, 0], [5, 1]
	]
}

TBlock = {
	"shape": [
		[0,0,0,0,1,1,1,0,0,0],
		[0,0,0,0,0,1,0,0,0,0]
	],
	"startPos": [
		[4, 0], [6, 1]
	]
}

ZBlock = {
	"shape": [
		[0,0,0,0,1,1,0,0,0,0],
		[0,0,0,0,0,1,1,0,0,0]
	],
	"startPos": [
		[4, 0], [6, 1]
	]
}

SBlock = {
	"shape": [
		[0,0,0,0,0,1,1,0,0,0],
		[0,0,0,0,1,1,0,0,0,0]
	],
	"startPos": [
		[4, 0], [6, 1]
	]
}

shapes = [IBlock, LBlock, OBlock, TBlock, ZBlock, SBlock]

def spawnBlock():
	global needToSpawn
	global blockPosRows
	# Get a random shape from the list
	spawnedBlock = random.choice(shapes)
	shape = spawnedBlock["shape"]

	# Set the shape in the game state
	for i in range(0, len(shape)):
		for j in range(0, len(shape[i])):
			gameState[i][j] = shape[i][j]

	blockPosRows = spawnedBlock["startPos"]
	needToSpawn = False

def printGameState():
	print("")

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
	print("Score:", gameScore)

# def checkForFullRows():
# 	global gameScore
# 	# Check each row
# 	for i in range(0, len(gameState)):
# 		# If the row is full
# 		if len(set(gameState[i])) == 1 and gameState[i][0] == -1:
# 			# Remove the row
# 			gameState.pop(i)
# 			# Add a new empty row
# 			gameState.insert(0, clearGameRow)
# 			# Increase the score
# 			gameScore += 1
# 			# Check for more full rows
# 			checkForFullRows()

# def checkForGameOver():
# 	if (-1 in gameState[0]):
# 		print("Game Over!")

def checkCollision(direction):
	if direction == "down":
		pass
	if direction == "left":
		pass
	if direction == "right":
		pass


def moveBlock(direction):
	global needToSpawn

	if direction == "down":
		# Only check the part of the gameState where the block is
		# Move the block from bottom up to avoid collision issues
		for i in range(len(blockPosRows) - 1, -1, -1):
			rowPos = blockPosRows[i]
			if rowPos + 1 > len(gameState) - 1:
				return
			
			blockRow = gameState[rowPos]

			for j in range(0, len(blockRow)):
				# If the current cell is part of the block
				if blockRow[j] == 1:
					# If the row below is part of the board
					if rowPos + 1 <= len(gameState) - 1:
						# The row below
						nextBlockRow = gameState[rowPos + 1]
						# If the cell below is not empty
						if nextBlockRow[j] == -1:
							return
						blockRow[j] = 0
						nextBlockRow[j] = 1
			# After moving down the row, move the pointer down
			blockPosRows[i] += 1
		
		# If the block has hit the bottom, spawn a new block
		if blockPosRows[-1] == len(gameState) - 1:
			needToSpawn = True

	if direction == "left":
		for i in blockPosRows:
			# Check if the block is at the left edge or has hit the bottom
			if gameState[i][0] != 0 or i == len(gameState) - 1:
				return
			# Shift the row to the left
			gameState[i] = gameState[i][1:] + [0]

	if direction == "right":
		for i in blockPosRows:
			# Check if the block is at the right edge or has hit the bottom
			if gameState[i][-1] != 0 or i == len(gameState) - 1:
				return
			# Shift the row to the right
			gameState[i] = [0] + gameState[i][:-1]

	if direction == "drop":
		for i in range(len(blockPosRows) - 1, -1, -1):
			rowPos = blockPosRows[i]
			blockRow = gameState[rowPos]

			for j in range(0, len(blockRow)):
				# If the current cell is part of the block
				if blockRow[j] == 1:
					endRow = rowPos - 2 + len(gameState)
					# If the row below is part of the board
					if endRow <= len(gameState) - 1:
						# The row below
						nextBlockRow = gameState[endRow]
						# If the cell below is not empty
						if nextBlockRow[j] != 0:
							return

						nextBlockRow[j] = -1
						blockRow[j] = 0

		needToSpawn = True

def promptForMove():
	move = input("Your move: ").lower()
	if move in ["left", "l"]:
		moveBlock("left")
	elif move in ["right", "r"]:
		moveBlock("right")
	elif move in ["drop", "d"]:
		moveBlock("drop")
	elif move != "":
		print("Unrecognized move")

def main():
	try:
		print(textris)
		print("Controls: left (l), right (r), drop (d)")
		# Game loop
		while True:
			if needToSpawn:
				spawnBlock()

			printGameState()

			promptForMove()

			moveBlock("down")
	except KeyboardInterrupt:
		print("\nExiting...")

if __name__ == "__main__":
	main()