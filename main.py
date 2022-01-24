'''
3. Feladat
Írj egy programot while ciklussal, amely kiírja a páratlan számokat csökkenő sorrendben 1 és 10 között!
'''


x = 10
while x > 0:
    if x %2 != 0:
        print(x)
    x -= 1