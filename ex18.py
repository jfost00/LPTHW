# This is like the argv

def printtwo(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# okay that *args is not needed

def printtwoagain(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument

def printone(arg1):
	print "arg1: %r" % arg1

# this takes nothing 

def printnone():
	print "I got nothing."
	
printtwo("Jeff", "CFE")
printtwoagain("Jeff", "CFE")
printone("ONE")
printnone()