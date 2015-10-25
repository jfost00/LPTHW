from sys import argv

sctipt, filename = argv

txt = open(filename)
print "Here's your file %r" % filename
print txt.read()

print "Type the filename again:"
fileagain = raw_input("> ")

txtagain = open(fileagain)

print txtagain.read()