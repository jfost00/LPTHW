x = "There are %d types of people." % 10
binary = "Binary"
donot = "don't"
y = "Those who know %s and those who %s." % (binary, donot)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
jokeeval = "Isn't that joke so funny?! %r"

print jokeeval % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w+e
