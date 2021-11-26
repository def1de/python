n=int(input('k='))
s=1
b=1
for i in range(1,n+1):
    s*=i
print(s)

a=1
while a<n+1:
    b*=a
    a+=1
print(b)
