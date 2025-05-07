def bubble_sort(arr):
    # storing the lengt of the array
    n = len(arr)
    # passing through the array
    for i in range(n):
        swapped = False
        # going through each plase of the array without the sortid elemnts
        for j in range(n -1 - i):
            #comparing the adjunct elements
            if arr[j] > arr[j+1]:
                #swapping the elements if they aren't in the correct order
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        # stop the alorihm if he made a full pass without doing any swaps
        if not swapped:
            break
    return arr
