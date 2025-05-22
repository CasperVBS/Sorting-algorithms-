def selection(arr):
    # strong the lengt of the array
    n = len(arr)
    # setting the max passes to the lengt of the array
    for i in range(n):
        # setting the smalest element on position i
        min = i
        # going through the un sortid array without the first (i) element
        for j in range(i+1,n):
            # compairing the element with the smalest element
            if arr[min] > arr[j]:
                # stroing the index of the smallest element
                min = j
        #Swap the smallest number with the element at the current index.
        arr[min] , arr[i] = arr[i], arr[min]
    return arr