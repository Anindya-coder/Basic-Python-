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
