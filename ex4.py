cars = 100
space = 4.0
drivers = 30
passengers = 90 
carsnotdriven = cars - drivers
carsdriven = drivers
carpool = carsdriven * space
avgpercar = passengers/carsdriven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", carsnotdriven, "empty cars today."
print "We can transport", carpool, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", avgpercar, "in each car."