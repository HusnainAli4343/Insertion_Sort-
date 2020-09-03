list = [3, 2, 5, 1, 4]
lenghtOflist = len(list)
rangeOflist = range(1,lenghtOflist)
for i in rangeOflist:
    numberTosort = list[i]
    while list[i-1] > numberTosort and i>0:
        temp = list[i]
        list[i] = list[i-1]
        list[i-1] = temp
        i-=1

print(list)
