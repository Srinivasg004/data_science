# Q. Declare a boolean value and store it in a variable.
# Check the type and print the id of the same.
a = False
print(type(a))
# Q. Take one boolean value between 0 - 256.
# Assign it to two different variables.
# Check the id of both the variables. It should come the same. Check why?
a=15
b=15
print(id(a))
print(id(b))

# Q. Arithmetic Operations on boolean data
# Take two different boolean values.
# Store them in two different variables.
# Do below operations on them:-
#  Find sum of both values
#  Find difference between them
#  Find the product of both.
#  Find value after dividing first value with second value
#  Find the remainder after dividing first value with second value
#  Find the quotient after dividing first value with second value
#  Find the result of first value to the power of second value.

a = True
b = False

print(a+b)
print(a-b)
print(a*b)
#print(a/b) - division by zero error
#print(a%b) - division by zero error
#print(a//b)- division by zero error
#print(a**b)- division by zero error

# Q. Comparison Operators on boolean values
# Take two different boolean values.
# Store them in two different variables.
# Do below operations on them:-
#  Compare these two values with below operator:-
#  Greater than, '>'
#  less than, '<'
#  Greater than or equal to, '>='
#  Less than or equal to, '<='
# Observe their output(return type should be boolean)
a = True
b = False

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# Q. Equality Operator
# Take two different boolean values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
# Observe the output(return type should be boolean)
a = True
b = False
print(a==b)
print(a!=b)

# Q. Logical operators
# Observe the output of below code
# Cross check the output manually
print(True and True)
#----------------------------------------->Output is True
print(False and True)
#----------------------------------------->Output is False
print(True and False)
#----------------------------------------->Output is False
print(False and False)
#----------------------------------------->Output is False
print(True or True)
#----------------------------------------->Output is True
print(False or True)
#----------------------------------------->Output is True
print(True or False)
#----------------------------------------->Output is True
print(False or False)
#----------------------------------------->Output is False
print(not True)
#----------------------------------------->Output is False
print(not False)
#----------------------------------------->Output is True

# Q. Bitwise Operators
# Do below operations on the values provided below:-
#  Bitwise and(&) --------------> True, True -------> Output is True
#  Bitwise or(|) --------------> True, False -------> Output is True
#  Bitwise(^) --------------> True, False -------> Output is True
#  Bitwise negation(~) ---------> True -------> Output is -2
#  Bitwise left shift ---------> True,2 -------> Output is 4
#  Bitwise right shift ---------> True,2 -------> Output is 0
# Cross check the output manually

a = True
b = False

print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)

# Q. What is the output of expression inside the print statement. Cross
# check before running the program.
a = True
b = True
print(a is b) #True or False? #
print(a is not b) #True or False?
a = False
b = False
print(a is b) #True or False?
print(a is not b) #True or False?

# Q. Membership operation
# in, not in are two membership operators and it returns boolean value
print(True in [10,10.20,10+20j,'Python', True])
print(False in (10,10.20,10+20j,'Python', False))
print(True in {1,2,3, True})
print(True in {True:100, False:200, True:300})
print(False in {True:100, False:200, True:300})