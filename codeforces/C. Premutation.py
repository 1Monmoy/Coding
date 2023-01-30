
import math as mt
 
 
def leastFrequent(arr, n):
 
    # Insert all elements in Hash.
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] += 1
        else:
            Hash[arr[i]] = 1
 
    # find the max frequency
    min_count = n + 1
    res = -1
    for i in Hash:
        if (min_count >= Hash[i]):
            res = i
            min_count = Hash[i]
 
    return res
def most_frequent(List):
    counter = 0
    num = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
 
    return num




t = int(input())
for l in range(t):
    s = []
    s2 = []
    n = int(input())
    for i in range(n):
        a = list(map(int, input().split()))
        s.append(a)

    for k in range(n-1):
        s1 = []
        for j in range(n):
            s1.append(s[j][k])
        # res = max(set(s1), key = s1.count)
        res = most_frequent(s1)
        res2 = leastFrequent(s1, len(s1))

        s2.append(res)
        if res != res2:
            s2.append(res2)
    s2 = list(dict.fromkeys(s2))
    new_lst=(' '.join(str(a)for a in s2))
    print(new_lst)
