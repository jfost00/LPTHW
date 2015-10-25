def cheeseandcrackers(cheesecount, boxesofcrackers):
	print "You have %d cheeses!" % cheesecount
	print "You have %d boxes of crackers!" % boxesofcrackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
print "We can just give the function numbers directly: "
	
cheeseandcrackers(20,30)
	
print "Or we can use variables from our script:"
cheeseamount = 10
crackersamount = 50 
	
cheeseandcrackers(cheeseamount, crackersamount)
	
print "We can even do math inside too: "
cheeseandcrackers(10+20, 5+6)

print "And we can combine the two, variables and math: "
cheeseandcrackers(cheeseamount + 100, crackersamount + 1000)

