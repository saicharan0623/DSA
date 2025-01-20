n=5
while n>=0:
    print(n*"*")
    n=n-1
    
i=1
while i<=5:
    print(i*"*")
    i=i+1

        
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end="")
    print('')
    
rows=5
for i in range(1,rows+1):
    print(end=" ")
    for j in range(1,i*1):
        print("*",end="")
    print('')

rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print('') 
    
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        if(j%2==1):
            print("*",end='')
        else:
            print("#",end='')  
            
    print('')


n=5
m=(2*n)-2
for i in range(0,n):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print("*",end=' ')
    print(" ")