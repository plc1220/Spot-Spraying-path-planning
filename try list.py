list1=[[1,1],[1.1,2],[1.2,3],[1.3,4]]

xlist = []

for i in range(len(list1)):
    x = list1[i][0]
    xlist.append(x)

    for j in xlist:
        if j == list1[i][0]:
            print(list1[i][1])
    
