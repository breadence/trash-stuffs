# Third upload


import pyperclip

clipboard = pyperclip.paste()

splitted = clipboard.split("\n")

returnboard = []

for line in splitted:

	if line.startswith("["):
		partitioned = line.partition("Willie:")
		toSave = partitioned[2]
		returnboard.append(toSave)
	else:
		returnboard.append(line)

joinedback = "\n".join(returnboard)

pyperclip.copy(joinedback)
