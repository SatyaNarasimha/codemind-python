a,b=map(int,input().split())
l=0
if a>b:
    l=a
    while(l):
        if(l%a==0 and l%b==0):
            print(l)
            break
        l+=1
else:
    l=b
    while(l):
        if(l%a==0 and l%b==0):
            print(l)
            break
        l+=1
    