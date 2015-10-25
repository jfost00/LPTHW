tenthings = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there aren't ten things in that list, let's fix that."
stuff = tenthings.split(' ')
morestuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	nextone = morestuff.pop()
	print "adding: ", nextone
	stuff.append(nextone)
	print "There's %d items now." % len(stuff)
	
print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])

