n=int(input())
v=[]
while n:
    v.append(n%10)
    n=n//10
if(len(v)==len(list(set(v)))):
    print('Unique Number')
else:
    print('Not Unique Number')