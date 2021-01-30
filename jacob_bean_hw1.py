#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jacob
#
# Created:     15/01/2021
# Copyright:   (c) Jacob 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def isLeap(year):
    if(year%100 == 0):
        if((year >=400) and (year%400 == 0)):
            return True
        return False
    elif(year%4 == 0):
        return True
    else:
        return False



def main():
    pass

if __name__ == '__main__':
    main()


year = int(input("enter year to check for leep year:"))\

while (year <=0):
    year = int(input("Invalid Year, please enter a new year above 0:"))


print("is the year "+ str(year) +" a leap year?")

if(isLeap(year) == True):
    print ("yes")
else:
    print("no")

input("Press any key to exit")