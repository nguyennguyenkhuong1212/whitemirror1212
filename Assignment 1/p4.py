# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Nguyen Khuong (s3924577)
# Created date: 16/11/2021
# Last modified date: 20/11/2021


import turtle

# initialize
win = turtle.Screen()
win.setup(width=700, height=1000, startx=0, starty=0)
tur = turtle.Turtle()
X = -200
Y = -300
tur.speed(10)


def get_total_num_of_pizzas(a, b, c, d):
    return a + b + c + d


def move(x, y):
    tur.up()
    tur.goto(x, y)
    tur.down()


def draw_x_y_axis(length):
    # set up the Turtle
    tur.color("Black")

    # draw x axis
    tur.setheading(90)
    tur.forward(length + 30)
    tur.stamp()

    # reset position
    move(X, Y)

    # draw y axis
    tur.setheading(0)
    tur.forward(180)
    tur.stamp()


def print_record_date(record_date):
    # move the turtle down a little bit
    move(X + 65, Y - 20)

    # print out the record date
    tur.write(record_date)

    # reset position
    move(X + 60, Y)


def draw_bar(length, color_string):
    # set color
    tur.color(color_string)

    # begin fill
    tur.begin_fill()

    # first line
    tur.setheading(90)
    tur.forward(length)

    # save the position of turtle to return
    x, y = tur.position()

    # second line
    tur.setheading(0)
    tur.forward(60)

    # third line
    tur.setheading(270)
    tur.forward(length)

    # end fill
    tur.end_fill()

    # move back
    move(x, y)


def write_total_num(a_num):
    # write the total number of pizzas on top of the bar chart
    tur.color("Black")
    tur.write(a_num)


def draw_bar_chart(record_date, large_thick, large_thin, medium_thick, medium_thin):
    # initial setting
    total_num = get_total_num_of_pizzas(large_thick, large_thin, medium_thick, medium_thin)
    tur.hideturtle()
    move(X, Y)
    scale = 8

    # draw x, y axis and print the record date
    draw_x_y_axis(total_num * scale)
    print_record_date(record_date)

    # draw four bar
    draw_bar(large_thick * scale, "#E51400")
    draw_bar(large_thin * scale, "#FA6800")
    draw_bar(medium_thick * scale, "#F0A30A")
    draw_bar(medium_thin * scale, "#E3C800")

    # write the total number of pizzas
    write_total_num(total_num)

def main():
    draw_bar_chart("16/11/2021", 20, 10, 15, 10)
    win.exitonclick()

main()
