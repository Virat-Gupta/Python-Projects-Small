# import colorgram

# colors = colorgram.extract('tutle painting/original.jpeg',30)

# rgb_colors = []
# for clr in colors:
#     r = clr.rgb.r
#     g = clr.rgb.g
#     b = clr.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)
import turtle as turtle_module
import random
color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171),
               (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), 
               (188, 80, 120), (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), 
               (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), 
               (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]


turtle_module.colormode(255)
draw_turtle = turtle_module.Turtle()
draw_turtle.speed("fastest")

draw_turtle.setheading(225)
draw_turtle.penup()
draw_turtle.fd(300)
draw_turtle.setheading(0)
draw_turtle.penup()
draw_turtle.hideturtle()
nextAngle = 180

for _ in range(10):
    for _ in range(10):
        draw_turtle.dot(20, random.choice(color_list))
        draw_turtle.fd(50)
    draw_turtle.back(50)
    draw_turtle.setheading(90)
    draw_turtle.fd(50)
    draw_turtle.setheading(nextAngle)
    nextAngle = (180 + nextAngle)%360

screen =turtle_module.Screen()
screen.exitonclick()