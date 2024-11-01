#
def triplelt(myNum):
    returnValue = myNum * 3
    myNum = myNum + 1 # this one have nothing to do in this block 'coz return returnValue (not return myNum)
    return returnValue


myNum = 6
newNum = triplelt(myNum)

print(newNum)

#
def doublet(a):
    a = a * 2
    return a

a = int(input("Input your number here: "))
print("a is:", a)
print("double a is:", doublet(a))

#
def doublet(b):
    b = b * 2
    return b
b = input("Over here: ")
print(doublet(b))


############################################
