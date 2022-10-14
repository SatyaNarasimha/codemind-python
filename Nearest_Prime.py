for k in range(int(input())):
    n=int(input())
    a=n
    while True:
        is_prime=True
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        else:
            a+=1
    b=n
    while True:
        is_prime=True
        for i in range(2,int(a**0.5)+1):
            if b%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        else:
            b=b-1
    if a-n < n-b:
        print(a)
    elif n-b == a-n:
        print(b)
    else:
        print(b)