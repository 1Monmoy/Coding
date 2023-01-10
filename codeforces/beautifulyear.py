year = input()
year = int(year) + 1
year = str(year)
def distinctvalue(year):
    count = 0
    c = 0
 
    for i in year:
        for j in range((c + 1), len(year)):
            if year[j] == i:
                count += 1
        
        c += 1
    if count > 0 :
        year = int(year) + 1
        year = str(year)
        distinctvalue(year)
    else:
        print(year)
distinctvalue(year)