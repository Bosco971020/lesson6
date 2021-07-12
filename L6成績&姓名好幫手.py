y=0
z=0
a=0
d=100000000000000000000000000000000000000
x=int(input('你需要輸入幾個成績?'))
score_list=[]
for i in range(0,x*2,2):         
    name = str(input('輸入新名字:'))
    y=int(input('輸入新成績:'))
    z=z+y
    if y > a:
        a=y
        h=i
    if y < d:
        d=y
        l=i
    score_list.append(y)
    score_list.append(name)
print('以上的成績平均是',z/x)
print('總成績為',z)
print('其中以',score_list[h],score_list[h+1],'分為最高分')
print('以',score_list[l],score_list[l+1],'分為最低分')