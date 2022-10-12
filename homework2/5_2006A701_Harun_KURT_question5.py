import turtle

def main(star:turtle.Turtle):
    while True:
        star.forward(step)
        star.left(135) #if we use 45 we are marked octo


if __name__ == '__main__':
    star=turtle.Turtle()
    step=100
    main(star)
