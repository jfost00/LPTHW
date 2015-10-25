from sys import argv
from os.path import exists

script, fromfile, tofile = argv

print "Copying from %s to %s" % (fromfile, tofile)

# we could do these two on the same line how?
infile = open(fromfile)
indata = infile.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(tofile)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

outfile = open(tofile, 'w')
outfile.write(indata)

print "Alright, all done."
outfile.close()
infile.close()