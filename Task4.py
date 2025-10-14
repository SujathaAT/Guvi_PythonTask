import random
from genericpath import isfile
from multiprocessing.dummy import current_process
from platform import python_build


#========================================================
#Question 1 Create Even and Odd number Lists
#========================================================
#pythonList = ("10","501","22","37","100","999","87","351")
pythonList = (10,501,22,37,100,999,87,351)
sizeofList = (pythonList.__len__())


even_number = []
odd_number = []
print(pythonList[0])
#number= pythonList[0]
#a= divmod(int(number),2)
j= 0
for i in pythonList:
    print(j)
    number = pythonList[j]
    a = divmod(int(number), 2)
    if a[1] == 0:
        even_number.insert(j,number)
        j=j+1
        print("Even Number")
       # break
    else:
        odd_number.insert(j, number)
        j = j + 1
        print("Odd Number")
    print("Even numbers are: ")
    print(even_number)
    print("")
    print("Odd numbers are: ")
    print(odd_number)
    if sizeofList == j:
        break



#========================================================
#Question 2 Find Prime Numbers
#========================================================


pythonList = (10,501,22,37,100,999,87,351,83)

prime_no= []
j= 0
#flag = False
for i in pythonList:

    for k in range(2,6):

        quotient, remainder = divmod(i, k)
        print(quotient)

        if remainder == 0:
            #flag = True
            print("Not Prime"+ str(i))
            break
        else:
            #print(j)
            print ("Prime "+ str(i))
            prime_no.insert(j, i)
            j = j + 1
            break

print (prime_no)
print(pythonList)

#========================================================
#Question 3 Find Happy Number
#========================================================


def find_happy(n):
    current_no = 0
    temp_no:list = []
    individual_no = str(n)
    #print(len(individual_no))
    for i in range(len(individual_no)):
        temp_no.insert(i, int(individual_no[i]) ** 2)

    for i in range(len(temp_no)):
        current_no =current_no + temp_no[i]
    #print(current_no)
    return current_no

strFlag = False
temp_no = 0

pythonList = ("19","501","22","37","100","999","87","351")
for k in range(len(pythonList)):
    n = pythonList[k]
    #print("Number " + n)
    for i in range(10):

        n = find_happy(n)
        temp_no = n

        if n == 1:
            print(str(pythonList[k]) + " is a Happy Number")
            strFlag = True
            break
        else:
            strFlag = False
    if not strFlag:
        print(str(pythonList[k]) + " is not a Happy Number")
#========================================================
#Question 4 First and Last number of and integer
#========================================================

number = 12345878778
current_number = str(number)
# print(current_number[0])
print("First number : " + current_number[0])
print("Last number : " + current_number[-1])
sum_fstnlst_intnos= int(current_number[0])+ int(current_number[-1])

print("Sum of first and last numbers : "+ str(sum_fstnlst_intnos))

#========================================================
#Question 5 Find all possible ways to make Rs.10
#========================================================
coin_list = [1,2,5,10]
final_amt = 10
counter  = 0
for a in coin_list:
    if a <= final_amt:
        comb_val = final_amt//a
        print(str(comb_val) + " coins of Rs." + str(coin_list[counter]) + " makes Rs."+ str(final_amt))
        counter += 1


#========================================================
# Question 6 Find duplicates in three lists
#========================================================


pythonList = [1,2,3,4,5]
pythonList1 = [1,2,3,7,8]
pythonList2 = [9,8,10]
duplicate_val = []
newList = pythonList+ pythonList1+pythonList2

checked_vals = set()
duplicate_vals = set()

for a in newList:
    if a in checked_vals:
        duplicate_vals.add(a)
    else:
        checked_vals.add(a)


print(f"Duplicates : {list(duplicate_vals)}")



#========================================================
# Question 7 Find  non repeating number in list
#========================================================

pythonList = [1,2,3,4,5]
pythonList1 = [1,2,3,7,8]
pythonList2 = [9,8,10]
duplicate_val = []
final_number = []
newList = pythonList+ pythonList1+pythonList2


checked_vals = set()
duplicate_vals = set()
nonrepeating_vals = set()

for a in newList:
    if a in checked_vals:
        duplicate_vals.add(a)
    else:
        checked_vals.add(a)

for a in newList:
    if a not in duplicate_vals:
        nonrepeating_vals.add(a)
        #print(f"Non repeating words : {list(nonrepeating_vals)}")
print(f"First Non repeating word : {(nonrepeating_vals.pop())}")

#========================================================
#Question 8 Minimum element in a rated sorted list
#========================================================

def get_element(movie_rates):
    minVal = (movie_rates["Movies"][0])
    return minVal

movie_rate = {"Movies": ["4","4.2", "4.8"]}
minRate = get_element(movie_rate)
print("Minimum element in a rated sorted list is :  " + minRate)


#========================================================
#Question 9 List sum is equal to value
#========================================================

gn_list = [10,20,30,9]
target_num = 59
num = 0
current_count = len(gn_list)
index_no = current_count-1
for i in range(3):

    # num = num + gn_list[index_no]
    if index_no != 0:
        num = num + gn_list[index_no]
        if num == target_num:
            print("Triplet is found: " + str(num))
        index_no = index_no - 1


#========================================================
#Question 10 Find Sublist sum is zero
#========================================================
check_list= [4,2,-3,1,6]
startind = 0
endind = 3
x= random.randint(0,len(check_list))
y= random.randint(0,len(check_list))

sublist = check_list[x:y]
if x < y and y!= len(check_list):
    # print(x)
    # print(y)
    # sumofvals = sum(sublist)
elif x ==y:
    x = random.randint(0, len(check_list))
    y = random.randint(0, len(check_list))
else:
    # print(x)
    # print(y)
    sublist = check_list[y:x]
sumofvals = sum(sublist)

print("Current Sublist Sum : " + str(sumofvals))
if sumofvals == 0:
    sumofvals = sum(sublist)
    print("Current Sublist " + str(sumofvals) + " sum is equal to zero")
else:
    print("Current Sublist sum is not zero")



