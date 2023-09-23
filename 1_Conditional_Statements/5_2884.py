a,b=input().split(" ")
a=int(a)
b=int(b)
if (b<45)&(a!=0):
    a-=1
    b=b+60-45
elif (b<45)&(a==0):
    a=23
    b = b + 60 - 45
else:
    b-=45
a=str(a)
b=str(b)
print(a+" "+b)