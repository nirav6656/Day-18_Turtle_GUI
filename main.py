from turtle import Turtle, Screen
import random
# Create a turtle object
t = Turtle()
t.color("green")
t.width(15)
t.shape("circle")
t.speed(10)
color_list = ["green","blue","red"]
angle_list = ["0","90","180","360"]

# Random Walk
for _ in range(0,100):
    t.color(random.choice(color_list))
    t.forward(25)
    t.left(int(random.choice(angle_list)))


# Combine Shape
# for i in range(3,10):
#     t.color(random.choice(color_list))
#     for _ in range(i):
#         angle = 180 - (((i-2)*180)/i)
#         t.forward(100)
#         t.left(angle)

# Triangle
# for _ in range(3):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(120)


# Square
# for _ in range(4):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(90)

# Pentagon
# for _ in range(5):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(72)


# Hexagon
# for _ in range(6):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(60)

# Heptagon
# for _ in range(7):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(51.43)

# Octagon
# for _ in range(8):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(45)

# Nonagon
# for _ in range(9):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(40)

# Decagon
# for _ in range(10):
#     t.color(random.choice(color_list))
#     t.forward(100)
#     t.left(36)



s = Screen()
s.exitonclick()
