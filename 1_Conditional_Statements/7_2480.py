a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)

if a==b==c:
    d=10000+a*1000
elif (a==b)|(b==c):
    d=1000+b*100
elif a==c:
    d=1000+a*100
elif a>b>c:
    d=a*100
elif a>c>b:
    d=a*100
elif b>a>c:
    d=b*100
elif b>c>a:
    d=b*100
elif c>a>b:
    d=c*100
else:
    d=c*100
print(d)