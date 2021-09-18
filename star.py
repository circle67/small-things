from math import cos, sin, radians
import matplotlib.pyplot as plt

poly = int(input("How many points should the star have? "))
point_turn = 360/poly/2
maj_radius = float(input("Major radius: "))
min_radius = float(input("Minor radius: "))

plot = input("Would you like the star plotted? (y/n) ") # plot or points
if 'y' in plot:
    plot = True
elif 'n' in plot:
    plot = False
else:
    plot = False

turn = 0
points = []
for x in range(poly):
    points.append([maj_radius * cos(radians(turn)), maj_radius * sin(radians(turn))])
    turn += point_turn
    points.append([min_radius * cos(radians(turn)), min_radius * sin(radians(turn))])
    turn += point_turn

if plot:
    points.append(points[0])

xs, ys = zip(*points)

if plot:
    plt.figure()
    plt.plot(xs, ys)
    plt.show()
else:
    for x in points:
        print("x: " + str(x[0]) + "\ty: " + str(x[1]))
