
strs = input().split()
a = []
output1 = []
output2 = ""
# min(strings, key=len)
output = []
count = True
a.append(min(strs, key=len))
strs.remove(a[0])
for k in range(len(a[0])):
    for i in range(len(strs)):
        # for j in range(k-1, len(strs[i])):
        #     if j<=len(a[0]):
        if a[0][k] == strs[i][k]:
            # output.append(a[0][k])
            count = True
        else:
            count = False
            break
    if count == False:
        break
    else:
        output.append(a[0][k])


print(output)
                
for i in range(len(output)):
            if output[i] == output[i]:
                output2+=output[i]
print(output2)


    






