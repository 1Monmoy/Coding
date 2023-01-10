from collections import Counter


year  = input()
year = int(year) + 1
year = str(year)
def finddistinctyear(year):

    distinctornot = Counter(year)
    if len(distinctornot) != len(year):
        year = int(year) + 1
        year = str(year)
        finddistinctyear(year)
    else:
        print(year)
finddistinctyear(year)

