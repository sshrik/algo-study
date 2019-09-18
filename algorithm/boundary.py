def lowerBound(arr, want, start=0, end=-1):
    # Init input.
    if end == -1:
        end = len(arr) - 1

    # If value is only 1, return it.
    if start == end:
        return arr[start]
    # Init values.
    length = end - start
    mid = start + int(length / 2)

    if arr[mid] < want:
        return lowerBound(arr, want, start=mid+1, end=end)
    elif arr[mid] >= want:
        # Need to return same or upper. And also, need to return first value of same numer.
        return lowerBound(arr, want, start=start, end=mid)

def upperBound(arr, want, start=0, end=-1):
    # Init input.
    if end == -1:
        end = len(arr) - 1

    # If value is only 1, return it.
    if start >= end:
        return arr[end]
    # Init values.
    mid = int((start + end) / 2)

    if arr[mid] <= want:
        return upperBound(arr, want, start=mid+1, end=end)
    elif arr[mid] > want:
        # Need to return same or upper. And also, need to return first value of same numer.
        return upperBound(arr, want, start=start, end=mid)

def lowerBoundIndex(arr, want, start=0, end=-1):
    # Init input.
    if end == -1:
        end = len(arr) - 1

    # If value is only 1, return it.
    if start == end:
        return start

    print("Start : " + str(start) + " End : " + str(end))
    # Init values.
    length = end - start
    mid = start + int(length / 2)

    if arr[mid] < want:
        return lowerBoundIndex(arr, want, start=mid+1, end=end)
    elif arr[mid] >= want:
        # Need to return same or upper. And also, need to return first value of same numer.
        return lowerBoundIndex(arr, want, start=start, end=mid)

def upperBoundIndex(arr, want, start=0, end=-1):
    # Init input.
    if end == -1:
        end = len(arr) - 1

    # If value is only 1, return it.
    if start >= end:
        return end
    # Init values.
    mid = int((start + end) / 2)

    if arr[mid] <= want:
        return upperBoundIndex(arr, want, start=mid+1, end=end)
    elif arr[mid] > want:
        # Need to return same or upper. And also, need to return first value of same numer.
        return upperBoundIndex(arr, want, start=start, end=mid)

print(upperBoundIndex([1,2,10,11,13,13,13,13,18,25,38,39,40,44], 11))
