a = [i+1 for i in range(50)][::-1] #массив и инверсия
for i in range(len(sides) - 2):
    side1 = sides[i]
    side2 = sides[i+1]
    side3 = sides[i+2]
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1) and (side1 != side2 and side2 != side3 and side1 != side3):
        hPerimetr = (side1 + side2 + side3) / 2
        print((hPerimetr * (hPerimetr - side1) * (hPerimetr - side2) * (hPerimetr - side3))**0.5, 'square')
        print(side1, side2, side3)
        break