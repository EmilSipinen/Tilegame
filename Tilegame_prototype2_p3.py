# python2 -u Tilegame_prototype2.py Subjectfile.txt

from sys import argv
script, file = argv
fileData = open(file)
content = str(fileData.read())

print ("\n")
print (content)

gameOver = False

fileData.close()

def indexList():
	# convert map file into usable form
	from sys import argv
	script, file = argv
	fileData = open(file)
	content = fileData.read()
	fileData.close()

	lines = content.splitlines()
	x_len = len(lines) # how long vertically the map is
	lenY = lines[0].split()
	y_len = len(lenY) # how long the map horisontaly is


	playerIndexPosition = content.find("@")
	# find index number of player

	# f check player surroundings and return what is there
	wIndex = playerIndexPosition - (y_len * 2 - 1)
	aIndex = playerIndexPosition - 1
	sIndex = playerIndexPosition + (y_len * 2 + 1)
	dIndex = playerIndexPosition + 3

	return [playerIndexPosition, wIndex, aIndex, sIndex, dIndex]

def contentList(indexList):
	# convert map file into usable form
	from sys import argv
	script, file = argv

	fileData = open(file)
	content = fileData.read()
	fileData.close()

	lines = content.splitlines()
	x_len = len(lines)# how long vertically the map is
	lenY = lines[0].split()
	y_len = len(lenY)# how long the map horisontaly is

	wIndex = indexList[1]
	aIndex = indexList[2]
	sIndex = indexList[3]
	dIndex = indexList[4]

	# f check player surroundings and return what is there
	wContent = content[wIndex - 1]
	aContent = content[aIndex - 1]
	sContent = content[sIndex - 1]
	dContent = content[dIndex - 1]

	return[content, wContent, aContent, sContent, dContent]

def newContent(content):
	print(content)

# f check validity of input
def wAction():
	content = contentList(indexList())

	wContent = content[1]

	if wContent == ".":
		canMove = True
	elif wContent == "#":
		canMove = False
	else:
		pass
	return [canMove]

def aAction():
	content = contentList(indexList())

	aContent = content[2]

	if aContent == ".":
		canMove = True
	elif aContent == "#":
	    canMove = False
	else:
	    pass
	return [canMove]

def sAction():
	content = contentList(indexList())

	sContent = content[3]

	if sContent == ".":
		canMove = True
	elif sContent == "#":
		canMove = False
	else:
		pass
	return [canMove]

def dAction():
	content = contentList(indexList())

	dContent = content[4]

	if dContent == ".":
		canMove = True
	elif dContent == "#":
		canMove = False
	else:
		pass
	return [canMove]

# f take player input
def inputW(contentList, indexList, action):

	content = contentList[0]
	wIndex = indexList[1]
	playerIndexPosition = indexList[0]

	# f update player w position
	if action[0] == True:
		global newContent
		newContent_ = content[:wIndex-1] + "@" + content[wIndex:]
		newContent = newContent_[:playerIndexPosition] + "." + newContent_[playerIndexPosition+1:]
		print ("")
		print (newContent)
	else:
		print ("You can't walk trough walls.\n")
		print (content)
	from sys import argv
	script, file = argv

	fileData = open(file, 'w')
	fileData.truncate()
	fileData.write(newContent)
	fileData.close()

def inputA(contentList, indexList, action):

	content = contentList[0]
	aIndex = indexList[2]
	playerIndexPosition = indexList[0]

	# f update player a position
	if action[0] == True:
		global newContent
		newContent_ = content[:aIndex-1] + "@" + content[aIndex:]
		newContent = newContent_[:playerIndexPosition] + "." + newContent_[playerIndexPosition+1:]
		print("")
		print(newContent)
	else:
		print("You can't walk trough walls.\n")
		print(content)

	from sys import argv
	script, file = argv

	fileData = open(file, 'w')
	fileData.truncate()
	fileData.write(newContent)
	fileData.close()

def inputS(contentList, indexList, action):
	#tileAction(sContent)

	# f update player s position

	content = contentList[0]
	sIndex = indexList[3]
	playerIndexPosition = indexList[0]

	# f update player s position
	if action[0] == True:
		global newContent
		newContent_ = content[:sIndex-1] + "@" + content[sIndex:]
		newContent = newContent_[:playerIndexPosition] + "." + newContent_[playerIndexPosition+1:]
		print("")
		print(newContent)
	else:
		print("You can't walk trough walls.\n")
		print(content)

	from sys import argv
	script, file = argv

	fileData = open(file, 'w')
	fileData.truncate()
	fileData.write(newContent)
	fileData.close()

def inputD(contentList, indexList, action):

	content = contentList[0]
	dIndex = indexList[4]
	playerIndexPosition = indexList[0]

	# f update player d position
	if action[0] == True:
		global newContent
		newContent_ = content[:dIndex-1] + "@" + content[dIndex:]
		newContent = newContent_[:playerIndexPosition] + "." + newContent_[playerIndexPosition+1:]
		print("")
		print(newContent)
	else:
		print("You can't walk trough walls.\n")
		print(content)

	from sys import argv
	script, file = argv

	fileData = open(file, 'w')
	fileData.truncate()
	fileData.write(newContent)
	fileData.close()

#---
def takeInput():
	i = input("\n>")
	inputCheck = bool(i != "w" or "a" or "s" or "d" or "exit")
	#print inputCheck

	if inputCheck == False:
		print("Uhh... What?")
		takeInput()
	elif i == "w":
		inputW(contentList(indexList()), indexList(), wAction())
	elif i == "a":
		inputA(contentList(indexList()), indexList(), aAction())
	elif i == "s":
		inputS(contentList(indexList()), indexList(), sAction())
	elif i == "d":
		inputD(contentList(indexList()), indexList(), dAction())
	elif i == "exit":
		exit()
	else:
		print("The valid controls are w, a, s, d for movement\nand exit for quiting the game.")
		takeInput()

#---
# driver code
while gameOver == False:
	#reloadFile()
	takeInput()
	#updateStatblock()

#---
fileData.close()

