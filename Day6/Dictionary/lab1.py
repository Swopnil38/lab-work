#Write a Python script to sort (ascending and descending) a dictionary by value. 
import operator
integer = {"first":1,"third":3,"fifth": 5,"second":2,"ninty":90}
sorted_integer = dict( sorted(integer.items(), key=operator.itemgetter(1)))
print(f"Dictionary in ascending order is {sorted_integer}")
sorted_integer = dict( sorted(integer.items(), key=operator.itemgetter(1),reverse=True))
print(f"Dictionary in Descending order is {sorted_integer}")
