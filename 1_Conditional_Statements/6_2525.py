a,b=input().split(" ")
c=input()
a=int(a)
b=int(b)
c=int(c)
d = b + c
e=d//60
if (d>=60)&(a+e<24):
    a=a+e
    b=d-e*60
elif (d>=60)&(a+e>=24):
    a=a+e
    a=a-24
    b = d - e * 60
else:
    b += c
a=str(a)
b=str(b)
print(a+" "+b)

