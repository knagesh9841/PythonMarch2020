
# Bubble Sort

MyList = [5, 3, 8, 6, 7, 2]

for i in range(len(MyList)):
    for j in range(len(MyList)-1):
        if MyList[j] > MyList[j+1]:
            tmp = MyList[j]
            MyList[j] = MyList[j+1]
            MyList[j+1] = tmp


print(MyList)
