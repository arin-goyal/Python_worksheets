# Type() function

a = 31
t = type(a)     # class<'int'>
print(t)

a = 31.12
t = type(a)     # class<'float'>
print(t)

a = "hello"
t = type(a)     # class<'str'>
print(t,"\n")

# Typecasting

a = "31.12"
b = float(a)
t = type(a)
t2 = type(b)
print(t)
print("b =",b)
print(t2)