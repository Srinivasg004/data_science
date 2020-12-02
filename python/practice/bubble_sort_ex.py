#sort the list

list = [3,5,2,1,4,9,8,6,10,7,11]
print('Before sorting the list', list)

def sortList(list):
    l = len(list)
    for i in range(l):
        for j in range(i+1,l):
            if list[i] > list [j]:
                t = list[i]
                list[i] = list[j]
                list[j] = t
sortList(list)
print('After sorting the list', list)