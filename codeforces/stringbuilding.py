t = int(input())
for i in range(t):
    s = input()
    l = len(s)
    a_counter = 0
    b_counter = 0
    error = 0
    if l > 1:
        if s[0] != s[1] or s[l-1] != s[l-2]:
            error+=1
    for i in range( len(s)):
        if s[i] == 'a':
            a_counter += 1
        if s[i] == 'b':
            b_counter += 1
    for i in range(1, len(s)-1):
        if s[i] != s[i-1] and s[i] != s[i+1]:
            error += 1

    if 0<a_counter<2 or 0<b_counter<2 or error>=1:
        print("NO")
    else:
        print("YES")