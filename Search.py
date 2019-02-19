# Binary search recursive version
def rec_binary_search(arr, ele):

    if len(arr) == 0:
        return False
    else:
        mid = int(len(arr)/2)

        if arr[mid] == ele:
            return True

        else:
            if ele < arr[mid]:
                return rec_binary_search(arr[:mid], ele)
            else:
                return rec_binary_search(arr[mid+1:], ele)


# Binary search iteration version
def binary_search(arr, ele):

    first = 0
    last = len(arr)-1
    found = False

    while first <= last and not found:
        mid = int((first+last)/2)
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = int(mid-1)
            else:
                first = int(mid+1)
    return found
