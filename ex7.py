print "Mary had a little lamb."
print "Its fleece was white as %s" % 'snow'
print "And everywhere that Mary went."
print "." * 10 # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "s"
end5 = "B"
end6 = "u"
end7 = "r"
end8 = "g"


# Watch that comma at the end try removing it and see what happens 

print end1 + end2 + end3 + end3 + end4 + end3,
print end5 + end6 + end7 + end8 + end3 + end7

# other stuff 
Cheese = end1 + end2 + end3 + end3 + end4 + end3
Burger = end5 + end6 + end7 + end8 + end3 + end7
CheeseBurger = Cheese + " " + Burger

print CheeseBurger

print '%r' % CheeseBurger * 100