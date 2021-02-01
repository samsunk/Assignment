# multiplication table
n=int(input('please enter the last number for multiplication:'))
m=int(input('please enter the last number of multiplicaton table'))
for i in range(1,n):
    for j in range(1,m):
        print(i,'*',j,'=',i*j)
    print()



