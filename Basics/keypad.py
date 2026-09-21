# WAP to make a 2D numpad as shown in a mobile 

row1 = (1, 2, 3)
row2 = (4, 5, 6)
row3 = (7, 8, 9)
row4 = ("*", 0, "#")

numpad =(row1, row2, row3, row4)
for rows in numpad :
    for column in rows :
        print(column, end=" ")
    print()