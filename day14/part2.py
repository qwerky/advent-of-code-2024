from Grid import Grid
from Robot import Robot
from time import sleep
import tkinter as tk
from tkinter import font

# What does a Christmas Tree look like? Who knows? I bet the elves do.
# Lets instead try to detect suspicious steps using a Chi-Squared test
# of the quadrant count we did for part 1. For a random distribution, the
# quadrants should all have a similar number of robots.
def step(val):
    grid.step(val)
    label.config(text=f"Step {grid.steps}")
    for sprite in sprites:
        robot = sprite[0]
        image = sprite[1]
        xPos = 10*robot.x
        yPos = 10*robot.y
        canvas.moveto(image, xPos, yPos)
    chiVal = grid.suspicious()
    if chiVal > 50:
        chiLabelValue.config(fg="red")
    else:
        chiLabelValue.config(fg="black")
    chiLabelValue.config(text=f'{chiVal:5.2f}')
    canvas.update()
    if chiVal > 50:
        sleep(2)

input = open("day14/input.txt", "r")
lines = input.read().splitlines()
seconds = 0

grid = Grid(101, 103)
for line in lines:
    robot = Robot(line)
    grid.robots.append(robot)

# Do the UI bit
window = tk.Tk()
window.title("Bathroom Robots")
window.geometry("1150x1150")

frame = tk.Frame(window, width=600, height=60, relief=tk.RAISED, borderwidth=4)
labelFont = font.Font(size=30)
label = tk.Label(frame, text="0", font=labelFont)
label.pack(side=tk.LEFT)
chiLabel = tk.Label(frame, text="  Chi test: ", font=labelFont)
chiLabel.pack(side=tk.LEFT)
chiLabelValue = tk.Label(frame, text="", font=labelFont)
chiLabelValue.pack(side=tk.LEFT)
frame.pack()


robotImage = tk.PhotoImage(file="day14/robot.png")
canvas = tk.Canvas(window, width="1010", height="1030")
canvas.pack()

sprites = []
for robot in grid.robots:
    xPos = 10*robot.x
    yPos = 10*robot.y
    image = canvas.create_image(xPos, yPos, image=robotImage)
    sprites.append((robot, image))


# Skip the boring bit
while grid.steps < 7600:
    grid.step(1)

while grid.steps < 10000:
    step(1)