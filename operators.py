
# arithmetic
a=20
b=10

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# assignment
a=15
a+=1
print(a)

a=15
a-=1
print(a)

a=15
a*=1
print(a)

a=15
a/=1
print(a)

a=15
a%=1
print(a)

a=15
a**=2
print(a)

a=15
a//=1
print(a)

# #comparison
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))

print(f'==:',(a==b))
print(f'>: ',(a>b))
print(f'<: ',(a<b))
print(f'!=: ',(a!=b))
print(f'>=: ',(a>=b))
print(f'<=: ',(a<=b))

# logical
a=True
b=False

print('AND: ',(a and b))
print('OR: ',(a or b))
print('NOT: ',(not a))

# bitwise
a = 15
b = 10

print(a & b)  
print(a | b)  
print(a ^ b)   
print(a << 2)  
print(a >> 2)  


# identity
x=10
y=20
z=10

print('x is z: ',x is z)
print('y is not z: ',y is not z)

# membership
characters=['eren','levi','lelouch']

print('eren in characters: ','eren' in characters)
print('dhoni not in characters: ','dhoni' not in characters)