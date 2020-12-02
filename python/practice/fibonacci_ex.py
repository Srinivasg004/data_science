#Fibonacci series
count = 1
i1, i2 = 0, 1
n =  int(input())
print('Fibonacci series of given number - ',n)

while count<=n:
    print(i1)
    x = i1+i2 
    i1 = i2
    i2 = x
    count+=1