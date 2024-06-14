import turtle
import time
import colorsys

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle instance
t = turtle.Turtle()
t.shape("blank")  # Set the turtle shape to blank (invisible)
t.speed(0)  # Set the drawing speed to maximum

# Define the line width
line_width = 5  # Change this value to adjust the line thickness

# Set the line width
t.width(line_width)

# Define the radius of the circles
radius = 50

# Define the number of circles to draw
num_circles = 13

# Define the angle between circles
angle = 360 / num_circles

# Define the color range
num_segments = 90  # Number of segments in each circle (reduced to a quarter)
hue_start = 0.0  # Starting hue value (0.0 to 1.0)
hue_end = 1.0  # Ending hue value (0.0 to 1.0)

# Draw the circles one by one
for i in range(num_circles):
    # Draw the circle with smooth color transition
    t.begin_poly()
    for j in range(num_segments):
        # Calculate the current hue value
        hue = hue_start + (hue_end - hue_start) * j / num_segments

        # Convert the hue value to RGB
        r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

        # Set the line color
        t.color(r, g, b)

        t.forward(radius * 4 * 3.14159 / 180)  # Move four times the distance
        t.left(4)  # Rotate four times the angle
    t.end_poly()

    # Rotate the turtle to the next position
    t.left(angle)

# Keep the window open until closed manually
turtle.done()