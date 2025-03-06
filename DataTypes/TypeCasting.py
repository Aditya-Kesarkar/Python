a = "20"
print(a,type(a)) # 20 <class 'str'>

b = int(a)
print(b, type(b)) # 20 <class 'int'>

print(type(int("100"))) # another way to do type-casting

# string to int conversion:
'''
In Python while converting string to int , only when string is holding int value to int 
conversion is allowed.
'''
print(int('12')) # 12
# print(int('code')) #Error
# print(int('12.44')) #Error
# print(int('True')) #Error

#WAC to take 2 float numbers from user and display its addition.
num1 = float(input('Enter num1  :'))
num2 = float(input('Enter num2  :'))
print(num1, type(num1), num2 , type(num2))
print('Addition is:',round(num1 + num2,2))

print(round(123.567890987,3))
print('{:.3f}'.format(123.567890987))

#bool():
print(bool(12)) # True -- int to bool conversion
print(bool(12.456)) # True --float to bool conversion
print(bool('Code')) # True -- string holding string to bool
print(bool(0)) # False -- int to bool
print(bool('')) # False  -- empty string to bool

#float():
print(float(123)) # 123.0 -- int to float conversion
#print(float('Code')) # Error -- string holding string to float 
print(float('123.23')) # 123.23 -- string holding float to float
print(float(True)) # 1.0 -- bool to float conversion
print(float(False)) # 0.0 -- bool to float conversion

#int():
print(int(123.55)) #123 -- float to int conversion
print(int('123')) #123 -- string holding int to int allowed
print(int(True)) #1 --boolean to int
print(int(False)) #0 --boolean to int
#print(int('Code')) #Error -- string holding string to int
#print(int('123.45')) #Error -- string holding float to int

'''
int('123.67') -- Not Allowed
int(123.67) -- Allowed
'''

num1 = int(input("Enter num1  :")) #10
num2 = int(input("Enter num2  :")) #2
print(num1/num2 ,type(num1/num2))  #5.0 <class 'float'>

# Whenever we are performing division operation the result will always be in float.
