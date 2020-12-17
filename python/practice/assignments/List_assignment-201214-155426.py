#Question 1: Given a Python list you should be able to display Python list in the following order
#aLsit = [100, 200, 300, 400, 500]
#Expected output:
#[500, 400, 300, 200, 100]

aList = [100, 200, 300, 400, 500]
#With inbuilt function
aList.reverse()
print(aList)


aList = [100, 200, 300, 400, 500]
#Using User defined function
def reverse_list(aList):
    l = 0
    r = len(aList)-1

    while l<r:
        t = aList[l]
        aList[l] = aList[r]
        aList[r] = t
        l += 1
        r -= 1
        
reverse_list(aList)
print(aList)



# Question 2: Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"] 
# list2 = ["y", "me", "s", "lly"]
# Expected output:
# ['My', 'name', 'is', 'Kelly']

# you code
list1 = ["M", "na", "i", "Ke"] 
list2 = ["y", "me", "s", "lly"]

#Using custom method
def concatinate_list_indx(list1, list2):
    l1 = len(list1)
    l2 = len(list2)
    l = 0
    new_list = []
    if l1 != 0 and l2 != 0:
        if l1 < l2:
            l = l1
            print(l)
        else:
            l = l2
            print(l)
    for i in range(l):
        print(i)
        new_list.insert(i,list1[i] + list2[i])
    
    return new_list

print(concatinate_list_indx(list1, list2))

#Using list comprehesion and zip

res = zip(list1, list2)
#zip creates the tuple by index wise. It is a iterable and works only one time
#Eg
#print(list(res))
#List comprehension
#[ expr for in source if condition]
print([i+j for i, j in res])

# Question 3: Given a Python list. Turn every item of a list into its square
# aList = [1, 2, 3, 4, 5, 6, 7]
# Expected output:
# [1, 4, 9, 16, 25, 36, 49]
# you code

aList = [1, 2, 3, 4, 5, 6, 7]
[i*i for i in aList]

# Question 4: Concatenate two lists in the following order   
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# you code
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = []
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        res.append(list1[i]+list2[j])
        
print(res)

# Question 7: Add item 7000 after 6000 in the following Python List 
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
# you code
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list2 = list1[2][2]# This is pointing to inner list
list2.insert(2,7000)
print(list1)

#Question 8: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list

# Given List:
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# Sub List to be added = ["h", "i", "j"]
# Expected output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
# you code
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist= ["h", "i", "j"]
list2 = list1[2][1][2]
list2.extend(sublist)
print(list2)
print(list1)
