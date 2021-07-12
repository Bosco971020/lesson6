x=int(input('輸入一個數字'))
a=0
ans=1
b=1
c=0
while b==1:
    for i in range(1,x+1):
        ans=ans*i
        c=c+ans
    x=x-1
    if x==1:
        ans=1
        b=1
    else:
        b=0
        print(c)
