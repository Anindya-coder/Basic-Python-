#bubble sorting 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  #flag 
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped = True
        #if no swap happened -> already sorted
        if not swapped:
            break
    return arr

#selection sorting
def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

#insertion sorting
def insertion_sorting(arr):
    n=len(arr)
    for i in range(1,n):
        insert_index = i
        current_value = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > current_value:
                arr[j+1] = arr[j]
                insert_index = j
            else:
                break 
        arr[insert_index] = current_value
    return arr

#another method for insertion sorting
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr

#merge sorting
def merge_sort(arr):
    #base case
    if len(arr) <= 1:
        return arr
    #divide the array
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    #merging the sub-arrays
    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0
    #comparing elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result 

#quick sort 
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j]<=pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[high] = arr[high], arr[i+1]
    
    return i+1

def quick_sort(arr,low,high):
    if low<high:
        p = partition(arr,low, high)
        
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
        #linked list

#for all linked list problems, we need to define a class that i have given below
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
#traversing a linked list        
def traverse(head):
        current_node = head
        while current_node:
            print(current_node.data, end = " ->")
            current_node = current_node.next
        print("null")
        
node1 = Node(1)

head = node1

traverse(head)

#counting the number of nodes in a linked list
def count_nodes(head):
    count = 0
    current_node = head
    while current_node:
        count += 1
        current_node = current_node.next
        
    return count

#finding the lowest value in a linked list

def find_minimum(head):
    if head is None:
        return None
    min_value = head.data
    current_node = head.next
    
    while current_node:
        if current_node.data < min_value:
            current_node.data = min_value
            current_node = current_node.next
    return min_value

#for finding the maximum value in a linked list, we can just change the variable name and condition to satisfy the requirement

#reversing a linked list
def reverse(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
    return prev

#deleting a value from a linked list

def delete_value(head,value):
    if not head:
        return None
    
    current = head
    if head.data == value:
        return head.next
    
    while current.next and current.next.data != value:
        current = current.next
        
    if current.next:
        current.next = current.next.next
        
    return head
        
