t = int(input())
for i in range(t):
    s = input()
    Alice = 0
    bob = 0
    if len(s) % 2 != 0:
        if s[len(s)-1] > s[0]:
            s = s[::-1]
        for i in range(len(s)-1):
            if s[i] =='a': Alice +=1
            if s[i] == 'b': Alice +=2
            if s[i] == 'c': Alice +=3
            if s[i] == 'd': Alice +=4        
            if s[i] == 'e': Alice +=5        
            if s[i] == 'f': Alice +=6        
            if s[i] == 'g': Alice +=7        
            if s[i] == 'h': Alice +=8        
            if s[i] == 'i': Alice +=9        
            if s[i] == 'j': Alice +=10        
            if s[i] == 'k': Alice +=11        
            if s[i] == 'l': Alice +=12
            if s[i] == 'm': Alice +=13
            if s[i] == 'n': Alice +=14
            if s[i] == 'o': Alice +=15
            if s[i] == 'p': Alice +=16
            if s[i] == 'q': Alice +=17
            if s[i] == 'r': Alice +=18
            if s[i] == 's': Alice +=19
            if s[i] == 't': Alice +=20
            if s[i] == 'u': Alice +=21
            if s[i] == 'v': Alice +=22
            if s[i] == 'w': Alice +=23
            if s[i] == 'x': Alice +=24
            if s[i] == 'y': Alice +=25
            if s[i] == 'z': Alice +=26
        for i in range(len(s)-1, len(s)):
            if s[i] =='a': bob +=1
            if s[i] == 'b': bob +=2
            if s[i] == 'c': bob +=3
            if s[i] == 'd': bob +=4        
            if s[i] == 'e': bob +=5        
            if s[i] == 'f': bob +=6        
            if s[i] == 'g': bob +=7        
            if s[i] == 'h': bob +=8        
            if s[i] == 'i': bob +=9        
            if s[i] == 'j': bob +=10        
            if s[i] == 'k': bob +=11        
            if s[i] == 'l': bob +=12
            if s[i] == 'm': bob +=13
            if s[i] == 'n': bob +=14
            if s[i] == 'o': bob +=15
            if s[i] == 'p': bob +=16
            if s[i] == 'q': bob +=17
            if s[i] == 'r': bob +=18
            if s[i] == 's': bob +=19
            if s[i] == 't': bob +=20
            if s[i] == 'u': bob +=21
            if s[i] == 'v': bob +=22
            if s[i] == 'w': bob +=23
            if s[i] == 'x': bob +=24
            if s[i] == 'y': bob +=25
            if s[i] == 'z': bob +=26
    else:
        for i in range(len(s)):
            if s[i] =='a': Alice +=1
            if s[i] == 'b': Alice +=2
            if s[i] == 'c': Alice +=3
            if s[i] == 'd': Alice +=4        
            if s[i] == 'e': Alice +=5        
            if s[i] == 'f': Alice +=6        
            if s[i] == 'g': Alice +=7        
            if s[i] == 'h': Alice +=8        
            if s[i] == 'i': Alice +=9        
            if s[i] == 'j': Alice +=10        
            if s[i] == 'k': Alice +=11        
            if s[i] == 'l': Alice +=12
            if s[i] == 'm': Alice +=13
            if s[i] == 'n': Alice +=14
            if s[i] == 'o': Alice +=15
            if s[i] == 'p': Alice +=16
            if s[i] == 'q': Alice +=17
            if s[i] == 'r': Alice +=18
            if s[i] == 's': Alice +=19
            if s[i] == 't': Alice +=20
            if s[i] == 'u': Alice +=21
            if s[i] == 'v': Alice +=22
            if s[i] == 'w': Alice +=23
            if s[i] == 'x': Alice +=24
            if s[i] == 'y': Alice +=25
            if s[i] == 'z': Alice +=26
    if Alice > bob:
        print("Alice", Alice-bob)
    else:
        print("Bob", bob-Alice)

