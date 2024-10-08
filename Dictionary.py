#OCT 8/2024
#The program below gets the first key in a dictionary
import sys
from multiprocessing.managers import view_type

dictionary  = dict(name="Samuel", age = 24, Course="Computer Science", Year = 3.2)
iteration = 1
for key in dictionary:
    print(key)
    break
#Sorting Dictionary by Key or Value
def sorted_dict(dic):
    srt =sorted(dic.values())
    return srt
dic = dict(name="Samuel", city = 'Nyeri', Course="Computer Science")
print(sorted_dict(dic))
#This program finds the sum of all items in a dictionary
dictionary =dict (x=24, y=16, z=36)
total = 0
for val in dictionary.values():
    total += val
print(total)
#Finding the size of bytes of a dictionary
dictionary  = dict(name="Samuel", age = 24, Course="Computer Science", Year = 3.2)
print(str(sys.getsizeof(dictionary)) + " " + "bytes")
#Merging Two dictionaries
dic1  = dict(name="Samuel", age = 24, Course="Computer Science", Year = 3.2)
dic2= dict(name="Samuel", city = 'Nyeri', Course="Computer Science")
dic1.update(dic2)
print(dic1)