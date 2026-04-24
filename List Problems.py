#get a list of smaller elements from a given integer comparing with given list
def get_smaller(l,s):
    res = []
    for x in l:
        if x < s:
            res.append(x)
    return res
l = [21, 34, 56, 74, 38,90]
s = 50
print(get_smaller(l,s))

#separate even odd number from a given list
def separate_even_odd(input_list):
    even = []
    odd = []
    for x in input_list:
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd 

input_list = [21, 34, 76, 89, 67,54]
even, odd = separate_even_odd(input_list)
print(even)
print(odd)

#average of list 
def get_average(input_list1):
    sum_of_elements = 0
    for x in input_list1:
        sum_of_elements += x
    number_of_elements = len(input_list1)
    average = sum_of_elements / number_of_elements
    return average 

input_list1 = [21, 45, 76,90]
print(get_average(input_list1))

#counting distinct elements in list
def distinct_elements(input_list2):
    count = 1
    for i in range (1, len(input_list2)):
        if input_list2[i] not in input_list2[:i]:
            count += 1
    return count 

number = [21, 21,45,78,90,90,67]
print(distinct_elements(number))

#extend the arithmetic progression 
def extendAP(arr):
    d = arr[1] - arr[0]
    for i in range(1, len(arr)):
        difference = arr[i] - arr[i-1]
        if difference != d:
            raise ValueError("Array is not a valid arithmetic progression")
    last = arr[-1]
    next_terms = tuple(last + d * i for i in range (1,4))
    return arr + next_terms

#checking if any array is sorted in increasing order
def isSorted(self, arr) -> bool:
        ascending = True
        for i in range(len(arr)-1):
            if ascending:
                if arr[i] > arr[i + 1]:
                    return False 
            else:
                if arr[i] < arr[i + 1]:
                    return False
        return True

#finding the index of key in an array(start, end)--- (-1,-1) for not having in the array 
def findIndex (self,arr, key ):
        #code here.
        start, end = 1, 1
        for i in range(len(arr)):
            if arr[i] == key:
                start = i
                break
            
        for i in range (len(arr) - 1, -1, -1):
            if arr[i] == key:
                end = i
                break 
            
        return [start, end]

#Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count

#given an array of integer 'arr', find out the count of pair (i,j) from array such that i < j and arr[i] > arr[j]

#method 1
#brute force method- applicable for small array but not for large array
def count_inversion(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                count += 1
    return count

#method 2
#merge shot algorithm for solving this problem
