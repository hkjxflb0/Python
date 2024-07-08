a = int(input("Enter number 1-"))
# b = int(input("Enter number 2 -"))


test_list = [1, 6, 3, 5, 3, 4]

##swapping first and last element

list1 = test_list
list1[0],list1[-1] = list1[-1],list1[0]
print(list1)

##reversing list
list2 = test_list
i = 0
j = len(list2) -1

while i < j:
    list2[i],list2[j] = list2[j],list2[i]
    i = i+1
    j = j-1

print(list2)

##Max element
print(max(list2))

## check number exists
if a in test_list:
    print(True)
else:
    print(False)

##generate random number
import random
list3 = []
for i in  range(20):
     l = random.randint(0,10)
     list3.append(l)
     
print(list3)   
##count unique element in list
lst = set(list3)
print(len(lst))

##permutation

from itertools import permutations

lste = permutations([4,2,5],3)
permute = [[]]
[permute.append(x) for x in lste]

##functions


a = 106

b = 20
print(locals().keys())  # Get local variables
print(globals().keys())  # Get global variables

# import required modules 
import inspect 

# use signature() 9

print(inspect.signature(len)) 

##print multiple argument
def fun(name, num): 
    print("Hello from ", name + ', ' + num) 
  
  
fun("netsmartz", "487") 



# define two methods 
 
# second method that will be returned
# by first method
def B(st2):
    print("Good " + st2 + ".")
  
# first method that return second method
def A(st1, st2):
    print(st1 + " and ", end = "")
     
    # return second method
    return B
 
# call first method that do two work:
# 1. execute the body of first method, and
# 2. execute the body of second method as 
#    first method return the second method
c = A("Hello", "Morning")
c("cmorning")     
