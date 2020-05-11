# Selection Sort

MyList = [5, 3, 8, 6, 7, 2]

for i in range(len(MyList)):
    minpos = i
    for j in range(i, len(MyList), 1):
        if MyList[j] < MyList[minpos]:
            minpos = j

    tmp = MyList[i]
    MyList[i] = MyList[minpos]
    MyList[minpos] = tmp

print(MyList)
