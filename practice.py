#Data types


## 1.Deinition:
##	 •    Data types are a classification of data which tell the compiler or interpreter how the programmer intends to use the data.
##   •    They determine the type of operations that can be performed on the data, values that the data can take, the amount of memory needed to store the data.



#integer Example
age = 35
type(age)

##floating point datatype
height = 5.11
print(height)
print(type(height))
bool("A")
a=10
b=10
type(a==b)
#string Data type
S='Welcome to the festival'

#check data type
print(type(S))
#access string with index
print(S[1])
print(S[2])
print(S[3])
## List  are similar to arrays found in other languages.
##   . They are  an ordered and mutable collection of items.
##   . list allows duplicates

#empty list
a=[]

# list with int values
# a[=1,2,3]
print(a)

b=["My", "name" "is","Adithya"]
print(b)
##Access list Items
a=["My", "name" "is","Adithya"]
print("Accesing element from the list")
print(a[0])
print(a[1])
## Accesing elements in reverse
a=["My", "name", "is","Adithya"]
print(a[-1])
print(a[-2])
## Tuple
## Def:Tuple is an ordered collection of python objects. Difference between tuple and list is that a tuple are immutable. Tuples cannot be modified after it os created
#Note: having one element is not sufficient it is a bit tricky. having one element in the parentheses is not sufficient, there must be a trailing 'comma' to make it a tuple.
#initiate empty tuple
tup1=()
tup2 = ('Geeks','For')
print("\nTuple with the use of string: ",tup2)
#Access Tuple items
tup1 = (1,2,3,4)
print(tup1[0])
print(tup1[1])
print(tup1[2])
## Set Data Type
#Definition: In Python Data Types. Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements.The orderof elements in a set is undefined though it may consist of various elements

#initializingempty set

s1=set()
s1=set("Adithya")
print("set with the uyse of string:",s1)
s2=set(["Hello","world"])
print("set with the use of list:",s2)
## Access Set items
#Set items cannot be accessed by refering to an index, since sets are unorderedf the items have no index. But we can loop through the set items using a for loop, or ask if a specified value is present in a set by using the key word in

Set1 = set(["Adithya","called","Adithya"])
print(Set1)

#loop through set

for i in Set1:
    print(i, end=" ") #prints elements one by one
print("Adithya" in Set1)

## Dictionary

#A dictionary in python is a collection of data avlues, used to store data values like a map unlike other datatypes

d={}
d={1:'Hi',2:"World"}
print(d)
#create dictionary using dict() constructore
d1 = dict({1:'GOKU',2:'calling',3:'RAJ'})
print(d1)
d1 = dict({1:'GOKU',2:'calling',3:'RAJ'})
print(d1[2])
