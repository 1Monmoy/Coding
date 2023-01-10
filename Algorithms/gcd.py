def gcd(m,n):
    while m!=n:
        if m>n:
            m = m-n
        else:
            n = n-m
    if m > n:
        print(m)
    else:
        print(n)
n = list(map(int, input().split()))
gcd(n[0], n[1])
