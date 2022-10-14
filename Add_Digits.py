a=int(input())
sum=0
while(a>0):
    r=a%10
    sum=sum+r
    a=a//10
    if sum>9 and a==0:
        a=sum
        sum=0
print(sum)