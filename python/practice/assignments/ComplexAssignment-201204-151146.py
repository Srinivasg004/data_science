# Q. Declare a complex number and store it in a variable.
# Check the type and print the id of the same.

a = 10 + 2j

print(type(a))

# Q. Arithmetic Operations on complex number
# Take two different complex numbers.
# Store them in two different variables.
# Do below operations on them:-
#  Find sum of both numbers
#  Find difference between them
#  Find the product of both numbers.
#  Find value after dividing first num with second number
#  Find the result of the first num to the power of the second number.

a = 15 + 25j
b = 10 + 15j

print('Sum of a',a,'and',b,'is',a+b)
print('Difference of a',a,'and',b,'is',a-b)
print('Product of a',a,'and',b,'is',a*b)
print('Division of a',a,'and',b,'is',a/b)
print('Power of a',a,'and',b,'is',a**b)

# Q. Comparison Operation not applicable between instance of complex
# values.
# Object reusability concept is not applicable on complex number


# Q. Equality Operator
# Take two different complex numbers.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
# Observe the output(return type should be boolean)

a = 10 + 15j
b = 5 + 5j

print(a==b)
print(a!=b)

# Q. Logical operators
# Observe the output of below code
# Cross check the output manually
print(10+20j and 20+30j) #20+30j
#----------------------------------------->Output is 20+30j
print(0+0j and 20+30j) #0+0j
#----------------------------------------->Output is 0j
print(20+30j and 0+0j) #0+0j
#----------------------------------------->Output is 0j
print(0+0j and 0+0j) #0+0j
#----------------------------------------->Output is 0j
print(10+20j or 20+30j) #10+20j
#----------------------------------------->Output is 10+20j
print(0+0j or 20+30j) #20+30j
#----------------------------------------->Output is 20+30j
print(20+30j or 0+0j) #20+30j
#----------------------------------------->Output is 20+30j
print(0+0j or 0+0j) #0+0j
#----------------------------------------->Output is 0j
print(not 10+20j) #False
#----------------------------------------->Output is False
print(not 0+0j) #True
#----------------------------------------->Output is True
# Q. What is the output of the expression inside the print statement.
# Cross check before running the program.
a = 10+20j
b = 10+20j
print(a is b) #False #True or False?
print(a is not b) #True #True or False?
# Q. Membership operation
# in, not in are two membership operators and it returns boolean value
print('2.7' in 'Python2.7.8') #True
print(10+20j in [10,10.20,10+20j,'Python']) #True
print(10+20j in (10,10.20,10+20j,'Python')) #True
print(30+40j in {1,20.30,30+40j}) #True
print(30+40j in {1:100, 2.3:200, 30+40j:300}) #True
print(10 in range(20)) #True