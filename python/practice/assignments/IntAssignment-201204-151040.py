#Q. Declare an int value and store it in a variable.
#Check the type and print the id of the same.

a = 10
print(type(a))
print(id(a))


#Q. Take one int value between 0 - 256.
#Assign it to two different variables.
#Check the id of both the variables. It should come the same. Check why?

b=5
c=5

print(id(b))
print(id(c))

# Q. Take one int value either less than -5 or greater than 256.
# Assign it to two different variables.
# Check the id of both the variables. It should come different.Check why?

d = 300
e = 300

print(id(d))
print(id(e))

# Q. Arithmetic Operations on integers
# Take two different integer values.
# Store them in two different variables.
# Do below operations on them:-
#  Find sum of both numbers
#  Find difference between them
#  Find the product of both numbers.
#  Find value after dividing first num with second number
#  Find the remainder after dividing first number with second number
#  Find the quotient after dividing first number with second number
#  Find the result of the first num to the power of the second number.

a = 5
b = 3

print('Sum of',a,'and',b, 'is',a+b)
print('Difference of',a,'and',b, 'is',a-b)
print('Product of',a,'and',b, 'is',a*b)
print('Division of',a,'by',b, 'is',a/b)
print('Remainder of',a,'by',b, 'is',a%b)
print('Quotient of',a,'by',b, 'is',a//b)
print('Power of',a,'pow',b, 'is',a**b)

# Q. Comparison Operators on integers
# Take two different integer values.
# Store them in two different variables.
# Do below operations on them:-
#  Compare se two numbers with below operator:-
#  Greater than, '>'
#  Smaller than, '<'
#  Greater than or equal to, '>='
#  Less than or equal to, '<='
# Observe their output(return type should be boolean)

a = 10
b = 5

print(a>b)
print(a>=b)
print(b>a)
print(b>=a)

if a>b:
    print(a,'is greater than',b)
if b<a:
    print(b,'is less than',a)    
if a>=b:
    print(a,'is greater than or equal to',b)
if b<=a:
    print(b,'is less than or equal to',a)
    
# Q. Equality Operator
# Take two different integer values.
# Store them in two different variables.
# Equate them using equality operators (==, !=)
# Observe the output(return type should be boolean)

a = 10
b = 20

print(a==b)
print(a!=b)

# Q. Logical operators
# Observe the output of below code
# Cross check the output manually
print(10 and 20)
#----------------------------------------->Output is 20
print(0 and 20)
#----------------------------------------->Output is 0
print(20 and 0)
#----------------------------------------->Output is 0
print(0 and 0)
#----------------------------------------->Output is 0
print(10 or 20)
#----------------------------------------->Output is 10
print(0 or 20)
#----------------------------------------->Output is 20
print(20 or 0)
#----------------------------------------->Output is 20
print(0 or 0)
#----------------------------------------->Output is 0
print(not 10)
#----------------------------------------->Output is False
print(not 0)
#----------------------------------------->Output is True

# Q. Bitwise Operators
# Do below operations on the values provided below:-
#  Bitwise and(&) -----------------------------------------> 10, 20
# -------> Output is 0
#  Bitwise or(|) -----------------------------------------> 10, 20
# -------> Output is 30
#  Bitwise(^) -----------------------------------------> 10, 20
# -------> Output is 30
#  Bitwise negation(~) ------------------------------------> 10
# -------> Output is -11
#  Bitwise left shift ------------------------------------> 10,2
# -------> Output is 40
#  Bitwise right shift ------------------------------------> 10,2
# -------> Output is 2
# Cross check the output manually

print(bin(10))
print(bin(20))

#10 bin- 01010
#20 bin- 10100
#10&20 - 00000
#output - 0
#print(int('00000',2))
print(10 & 20)

#10 bin- 01010
#20 bin- 10100
#10|20 - 11110
#output - 30 
#print(int('11110',2))
print(10 | 20)

print(10^20)
print(~10)
print(10<<2)
print(10>>2)

# Q. What is the output of expression inside print statement. Cross check
# before running the program.
a = 10
b = 10
print(a is b) #True or False?
print(a is not b) #True or False?
a = 1000
b = 1000
print(a is b) #True or False?
print(a is not b) #True or False?


#Q. What is the output of expression inside print statement. Cross check
#before running the program.
print(10+(10*32)//2**5&20+(~(-10))<<2)

# Q. Membership operation
# in, not in are two membership operators and it returns boolean value
print('2' in 'Python2.7.8')
print(10 in [10,10.20,10+20j,'Python'])
print(10 in (10,10.20,10+20j,'Python'))
print(2 in {1,2,3})
print(3 in {1:100, 2:200, 3:300})
print(100 in {1:100, 2:200, 3:300})
print(10 in range(20))

# Q. An integer can be represented in binary, octal or hexadecimal form.
# Declare one binary, one octal and one hexadecimal value and store them
# in three different variables.
# Convert 9876 to its binary, octal and hexadecimal equivalent and print
# their corresponding value.

a=9876

ab = bin(a)
ao = oct(a)
ah = hex(a)

print(a)
print('Binary conversion of',a,'is',ab)
print('Octal conversion of',a,'is',ao)
print('Hexadecimal conversion of',a,'is',ah)

#Q. What will be the output of following:-
a = 0b1010000
print(a)
b = 0o7436
print(b)
c = 0xfade
print(c)
print(bin(80))
print(oct(3870))
print(hex(64222))
print(bin(0b1010000))
print(bin(0xfade))
print(oct(0xfade))
print(oct(0o7436))
print(hex(0b1010000))
print(hex(0xfade))