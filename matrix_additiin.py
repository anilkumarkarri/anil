print("enter the elements into the 1st matrix :")
a=[]
for i in range(3):
   a1=[]
   for j in range(3):
     input1=int(input())
     a1.append(input1)
   a.append(a1)
print(a)
print("enter the elements into the 2nd matrix :")
b=[]
for i in range(3):
    b1=[]
    for j in range(3):
       input2=int(input())
       b1.append(input2)
    b.append(b1)
print(b)    
r=[]
for i in range(3):
    sum_subList=[]
    for j in range(3):
       summ=a[i][j]+b[i][j]
       sum_subList.append(summ)
    r.append(sum_subList)
print("addition of 2 matrices :")
print(r)


