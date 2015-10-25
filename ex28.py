"""
1. True and True is True
2. False and True is False
3. 1 == 1 and 2 == 1 is True and False is False
4. "test" == "test" is True
5. 1 == 1 or 2 != 1 is True
6. True and 1 == 1 is True
7. False and 0 != 0 is False and False is False
8. True or 1 == 1 is True
9. "test" == "testing" is False 
10. 1 != 0 and 2 == 1 is True and False is False
11. "test" != "testing" is True
12. "test" == 1 is False
13. not (True and False) is True
14. not (1 == 1 and 0 != 1) is False
15. not (10 == 1 or 1000 == 1000) is not(true or false) is not(true) is false
16. not (1 != 10 or 3 == 4) is not(true or false) is not(true) is false
17. not("testing" == "testing" and "Zed" == "Cool Guy") is not(true and false) is not(false) is true
18. 1 == 1 and not("testing" == 1 or 1 == 0) is true and not(false or false) is true and true is true
19. "chunky" == "bacon" and not(3 == 4 or 3 == 3) is false and not(false or true) is false and false is false
20. 3 == 3 and not("testing" == "testing" or "Python" == "Fun") is true and not (true or false) is true and not(true) is true and false is false
"""

print "1. my answer: True, real answer: ", True and True
print "2. my answer: False, real ansewr: ", False and True
print "3. my answer: False, real answer: ", 1==1 and 2==1
print "4. my answer: True, real answer: ", "test" == "test"
print "5. my answer: True, real answer: ", 1==1 or 2!=1
print "6. my answer: True, real answer: ", True and 1==1
print "7. my answer: False, real answer: ", False and 0!=0
print "8. my answer: True, real answer: ", True or 1==1
print "9. my answer: False, real answer: ", "test" == "testing"
print "10. my answer: False, real answer: ", 1 != 0 and 2 == 1
print "11. my answer: True, real answer: ", "test" != "testing" 
print "12. my answer: False, real answer: ", "test" == 1
print "13. my answer: True, real answer: ", not(True and False)
print "14. my answer: False, real answer: ", not(1==1 and 0!=1)
print "15. my answer: False, real answer: ", not(10 == 1 or 1000 == 1000)
print "16. my answer: False, real answer: ", not(1!=10 or 3==4)
print "17. my answer: True, real answer: ", not("testing" == "testing" and "Zed" == "Cool Guy")
print "18. my answer: True, real answer: ", 1==1 and not("testing" == 1 or 1 == 0)
print "19. my answer: False, real answer: ", "chunky" == "bacon" and not(3 == 4 or 3 == 3)
print "20. my answer: False, real answer: ", 3 == 3 and not("testing" == "testing" or "Python" == "Fun")




