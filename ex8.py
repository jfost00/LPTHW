formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.", 
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)
	

# This works! cool	
print formatter % (formatter % (1,2,3,4), formatter % (5,6,7,8), formatter % (9,10,11,12), formatter % (13,14,15,16))