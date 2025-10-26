
#========================================================
#Question 1 Map people not under 18 in new list from list of dictionary
#========================================================
people = [
    {"name": "Tom", "age": 100},
    {"name": "Jerry", "age": 90},
    {"name": "Hellokitty", "age": 10}
]
a   = list(map(lambda x: x['age'] if x['age'] < 18 else x['name'],people))
print(a)
newval = []
for x in a:
    if type(x) != int:
        print(x)
        newval.append(x)

print(f"People not under 18 are {newval}")

#==========================================================================
#Question 2 Calculate product of all numbers inlist using reduce  function
#           Using lambda function
##==========================================================================

from functools import reduce

numlist = [10,29,3,50,2,15,80]

newnumlist = reduce(lambda x,y: x*y, numlist)
print("Product of list of numbers is ")
print(newnumlist)

#====================================================================
#Question 3 Create new list of squares only for even number from list
#           Using lambda function
#====================================================================

no1 = [10,29,3,50,2,15,80]
evensquare = []
# print(no)
for no in no1:
    chkeven = lambda no : no % 2

    if chkeven(no) == 0:
        print(str(no) + "number is an even number")
        a= lambda x: evensquare.append(x**2)
        a(no)
        # print(evensquare)
    else:
        print(str(no) + "number is not an even number")

print(f"Squares of even numbers list: {evensquare}")


#==========================================================================
#Question 4 Check given string is a number
#           Using lambda function
#===========================================================================
import string
number = input("Enter a string  :")
checkvaltype = lambda no: type(no) == str

if (checkvaltype(number) == False):
    # print(type((number)))
    print(str(number) + "Value is not a string ")
else:
    print(str(number) + "Value is a string ")


#==========================================================================
#Question 5 Extract year, month,day from datetimeobjects
#           Using lambda function
#==========================================================================
import datetime

dateobj= datetime.datetime.today()
getyr = lambda dtob : dtob.year
getmth = lambda dtob : dtob.month
getday = lambda dtob : dtob.day


print(f"Current year  {getyr(dateobj)}")
print(f"Current month {getmth(dateobj)}")
print(f"Current month {getday(dateobj)}")

# ==========================================================================
# Question 6 Generate Fibonacci series upto n terms
#           Using lambda function
# ==========================================================================
ntime = 10
result = [0, 1]
list_length = (len(result))
abc = (result[list_length-1] + result[list_length-2])

newresult = (lambda result: result.append(abc))
for a in range(0,ntime):
    newval = newresult(result)
    list_length = (len(result))
    abc = (result[list_length - 1] + result[list_length - 2])
print(f" Fibonacci series for n terms  : {result}")

