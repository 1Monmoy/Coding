
s = input()
n = len(s)
res = []
i = 0
while i < n:
    if (i+1) == (n)  and s[i] == ".":
        res.append(0)
        break
    if s[i] == "." and s[i+1] == ".":
        res.append(0)
    if s[i] == "." and s[i+1] == "-":
        res.append(0)
    if s[i] == "-" and s[i + 1] == ".":
        res.append(1)
        i += 1
    if s[i] == "-" and s[i + 1] == "-":
        res.append(2)
        i += 1
        
    i += 1
print(''.join(map(str,res)))

