import numpy as np
import matplotlib.pyplot as plt
import csv
from tabulate import tabulate

solutions = []
circles = []
data = []
file_name = input("Enter the name of the file to be created/read - ")

def write_csv_file(file_name):
    f = open(file_name, "w", newline = "")
    cf = csv.writer(f, delimiter = ",")
    for i in range(3):
        x = int(input("Enter x-coordinate of circle " + str(i+1) + " - "))
        y = int(input("Enter y-coordinate of circle " + str(i+1) + "  - "))
        r = int(input("Enter radius of circle " + str(i+1) + " - "))
        L = [x,y,r]
        cf.writerow(L)
    f.close()

def read_csv_file(file_name):
    global data
    f = open(file_name, "r")
    contents = csv.reader(f, delimiter = ",")
    for i in contents:
        data.append(i)
    return data

def calculate_apollonius():
    global x1,x2,x3,y1,y2,y3,r1,r2,r3
    x1 = int(data[0][0])
    y1 = int(data[0][1])
    r1 = int(data[0][2])
    x2 = int(data[1][0])
    y2 = int(data[1][1])
    r2 = int(data[1][2])
    x3 = int(data[2][0])
    y3 = int(data[2][1])
    r3 = int(data[2][2])
    for i in [1, -1]:
        for j in [1, -1]:
            for k in [1, -1]:
                a1 = 2 * (x1 - x2)
                b1 = 2 * (y1 - y2)
                c1 = 2 * (i*r1 - j*r2)
                d1 = (x1**2 + y1**2 - r1**2) - (x2**2 + y2**2 - r2**2)

                a2 = 2 * (x1 - x3)
                b2 = 2 * (y1 - y3)
                c2 = 2 * (i*r1 - k*r3)
                d2 = (x1**2 + y1**2 - r1**2) - (x3**2 + y3**2 - r3**2)
                
                try:
                    e1 = (d1*b2 - d2*b1) / (a1*b2 - a2*b1)
                    f1 = (c1*b2 - c2*b1) / (a1*b2 - a2*b1)
                    e2 = (a1*d2 - a2*d1) / (a1*b2 - a2*b1)
                    f2 = (a1*c2 - a2*c1) / (a1*b2 - a2*b1)

                    coeff = [f1**2+f2**2-1, -2*(f1*(e1-x1)+f2*(e2-y1)+i*r1), (e1-x1)**2+(e2-y1)**2-r1**2]
                    
                    roots = np.roots(coeff)
                    for l in range(len(roots)):
                         if np.isreal(roots[l]):
                            r = np.round(np.real(roots[l]),2)
                            if r>0:
                                x = e1 - r*f1
                                y = e2 - r*f2
                                if [(x,y),r] not in [[(x1,y1),r1], [(x2,y2),r2], [(x3,y3),r3]]:
                                    circles.append([(x,y),r])
                                    solutions.append([x,y,r,i,j,k])
                except ZeroDivisionError:
                    print("No Apollonius circles exist for", i, j, k)
                
    return circles
               
def plotting_circles():
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    for original_circles in [[(x1,y1),r1], [(x2,y2),r2], [(x3,y3),r3]]:
        Drawing_circle = plt.Circle(original_circles[0], original_circles[1], edgecolor = "blue", linewidth = 1, fill = False)
        axes.add_artist(Drawing_circle)
    for apollonius_circles in circles:
        Drawing_circle = plt.Circle(apollonius_circles[0], apollonius_circles[1], edgecolor = "red", linewidth = 1, fill = False)
        axes.add_artist(Drawing_circle)
        
def main():
    read_csv_file(file_name)
    calculate_apollonius()
    print()
    print(tabulate(solutions, headers = ["Center x-coordinate", "Center y-coordinate", "Radius", "i", "j", "k"]))
    plotting_circles()
    plt.show()
    
main()
