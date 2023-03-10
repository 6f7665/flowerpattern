import sys
import math

#the size will be 300 x 300
num_of_args = len(sys.argv)

#setting amount of petals
try:
    if sys.argv[1] < 3:
        print(f"can't have less than 3 petals, setting 3")
        flower_petal_amount = 3
    else:
        flower_petal_amount = int(sys.argv[1])
except:
    flower_petal_amount = 5
#inner diameter
try:
    diameter = int(sys.argv[2])
except:
    diameter = 40 #petals are 20 from the center

#setting the amount of offset (curve)
try:
    offset = int(sys.argv[3])
except:
    offset = 10 #10 away from petal is the bevel point
#setting offset distance
try:
    offset_distance = int(sys.argv[4])
except:
    offset_distance = 20 #distance from the point out on the bevel

radius = diameter / 2

#we slice the part in the middle into pizza slices and calc the distance between each cut at the outer crust
def calc_base_of_triangle(angle, vert_lenght):
    #a/sin A = b/sin B = c/sin C
    A = angle / 2
    B = 90 - A
    C = 90
    c = vert_lenght
    #a/sin A = c/sin C => a = (c/sinC) * sinA <=>/sinC=1/<=> a = c * sinA
    a = (c * math.sin(math.radians(A)))

    return a



class petal_class:
    def __init__(self, angle):
        print(str(angle))

def main():
    print("program started")
    petal_list = []
    for i in range(flower_petal_amount):
        petal_list.append(petal_class(i * (360 / flower_petal_amount)))
    print(str(calc_base_of_triangle((360 / flower_petal_amount), diameter)))

main()