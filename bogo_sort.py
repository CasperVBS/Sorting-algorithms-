import random

def bogo_sort(arr):
    attempt = 0
    # repeat until the array is sorted
    while not is_sorted(arr):
        # shuffle the array in random order
        random.shuffle(arr)
        attempt += 1
        #print(attempt)
    # when it's finnisched return the sorted array
    return arr,attempt
# checking if the array is sorted
def is_sorted(arr):
    sorted = True
    # going through each plase of the array 
    for i in range(len(arr)-1):
        #comparing the adjunct elements
        if arr[i]>arr[i+1]:
            # if the array is sorted break out the loop 
            sorted = False
            break
    #return if the array is sorted
    return sorted