import turtle
import math

screen = turtle.Screen()
screen.title("Pythagorean Tree")

t = turtle.Turtle()
t.speed(0)

def draw_pythagorean_tree(t, length, angle, level):
    if level == 0:
        return

    t.forward(length)
    new_length = length * (1 / math.sqrt(2))

    t.left(angle)
    draw_pythagorean_tree(t, new_length, angle, level - 1)

    t.right(2 * angle)

    draw_pythagorean_tree(t, new_length, angle, level - 1)

    t.left(angle)
    t.backward(length)

def main():
    length = 100
    angle = 45
    
    try:
        level = int(input("Recursion level (recommended 5-10): "))
    except ValueError:
        print("Enter integer please.")
        return

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    draw_pythagorean_tree(t, length, angle, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
