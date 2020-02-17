from cs1lib import *

# starting and end points of stick
x1a = 50
y1a = 200
x2a = 150
y2a = 350
x1b = 360
y1b = 20
x2b = 320
y2b = 250
num_strings = 36

# main drawing function
def draw_string_art():
    set_clear_color(0,0,0)
    clear()
    draw_sticks()
    draw_strings()


# draws strings
def draw_strings():

    set_stroke_width(1)
    f = 0

    # change in f from one string to the next
    change = (1 / (num_strings -1))

    while f <= (1 + change):

        # changes color from string to string
        set_stroke_color(0, f, .9)

        # sets tacks based on f value
        xa = x1a + f * (x2a - x1a)
        ya = y1a + f * (y2a-y1a)
        xb = x1b + (1.0 - f) * (x2b - x1b)
        yb = y1b + (1.0 - f) * (y2b - y1b)

        # draws new string
        draw_line(xa,ya,xb,yb)

        # increments f to draw the next string
        f = f + change


# draws two red sticks
def draw_sticks():
    set_stroke_width(3)
    set_stroke_color(1, 0, 0)
    draw_line(x1a, y1a, x2a, y2a)
    draw_line(x1b, y1b, x2b, y2b)

# main function that calls drawing function
def main():
    draw_string_art()


start_graphics(main)