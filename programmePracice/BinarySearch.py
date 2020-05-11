# Binary Search List should be in sorted Order

pos = -1


def binarysearch(mylist, element):
    lower = 0
    upper = len(mylist) - 1
    while lower <= upper:
        mid = (lower + upper) // 2

        if mylist[mid] == element:
            globals()['pos'] = mid
            return True
            break
        elif element < mylist[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
    else:
        return False


MyList = [5, 7, 99, 100, 120, 300, 456, 800, 1010, 1200, 9999, 11111]

if binarysearch(MyList, 70):
    print("Element is found at Location ", pos+1)
else:
    print("Element is not found")

