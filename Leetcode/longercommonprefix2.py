class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = []
        output1 = []
# min(strings, key=len)
        output = []
        a.append(min(strs, key=len))
        strs.pop(0)
        for k in range(len(a[0])):
            for i in range(len(strs)):
                for j in range(k-1, len(strs[i])):
                    if j<=len(a[0]):
                        if a[0][k] == strs[i][j]:
                            output.append(a[0][j])
                
        for i in range(len(output)-1):
            if output[i] == output[i+1]:
                output1.append(output[i])
        print(output1)
