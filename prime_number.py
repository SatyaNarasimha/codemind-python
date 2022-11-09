ab=int(input())
l=0
for r in range(1,ab+1):
    if ab%r==0:
        l+=1
if l==2:
    print('prime')
else:
    print('not a prime')