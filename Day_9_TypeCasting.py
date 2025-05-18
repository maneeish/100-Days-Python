#Implicit typecasting
a = 10        # int
b = 2.5       # float

result = a + b
print(result)        # 12.5
print(type(result))  # <class 'float'>

#Explicit Typecasting
x = "100"
y = int(x)     # string to int
print(y + 50)  # 150

a = 5
b = str(a)     # int to string
print(b + "0") # "50"


