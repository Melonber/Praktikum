import tkinter as tk
import math

def create_object(array):
    x1, y1, x2, y2 = pos_coords(array)
    return canv.create_oval(x1, y1, x2, y2, fill="white")

def animate():
    oval_2[4] += oval_2[5]
    moves(e_id, oval_2)
    main.after(speed, animate)

def pos_coords(array):
    x_coord, y_coord, radius, space, angle, speed_of_angle, x, y = array
    x = x_coord - space * math.sin(math.radians(-angle))
    y = y_coord - space * math.cos(math.radians(-angle))
    array[6] = x
    array[7] = y
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius
    print(array)
    return x1, y1, x2, y2


def moves(object_id, array):
    x1, y1, x2, y2 = pos_coords(array)
    canv.coords(object_id, x1, y1, x2, y2)

speed = 5
side_circle = 1 


oval_1 = [300, 300, 200, 0, 0, 0, 0, 0]
oval_2 = [300, 300, 20, 200, 0, side_circle, 0, 0]

main = tk.Tk()
main.title("tkinter")

canv = tk.Canvas(main, width=600, heigh=600, bg="black")
canv.pack()

create_object(oval_1)
e_id = create_object(oval_2)
main.geometry('600x600')

animate()

main.mainloop()
