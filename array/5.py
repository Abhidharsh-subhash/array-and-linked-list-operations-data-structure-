#extend python array using extend() method

from array import *

arr1=array('i',[1,2,123,4,5])
arr2=array('i',[11,12,13,14])
print(arr2)
arr2.extend(arr1)
print(arr2)