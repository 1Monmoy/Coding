n = int(input())
for i in range (n):
    a = int(input())
    if a >= 1900:
        print('Division 1')
    if a>=1600 and a<=1899:
        print('Division 2')
    if a>=1400 and a<=1599:
        print('Division 3')
    if a<=1399:
        print('Division 4')
