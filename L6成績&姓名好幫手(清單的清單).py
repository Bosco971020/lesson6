y=0
z=0
a=0
d=100000000000000000000000000000000000000
x=int(input('你需要輸入幾個成績?'))
score_list=[]
for i in range(x):         
    name=str(input('輸入新名字:'))
    y=int(input('輸入新成績:'))
    z=z+y
    if y > a:
        a=y
        h=i
    if y < d:
        d=y
        l=i
    i=[]
    i.append(name)
    i.append(y)
    score_list.append(i)
print('以上的成績平均是',z/x)
print('總成績為',z)
print('其中以',score_list[h],'分為最高分')
print('以',score_list[l],'分為最低分')