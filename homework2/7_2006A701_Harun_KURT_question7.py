import turtle

def main(star:turtle.Turtle):
    star.write("STOP",align="center")
    star.up()
    star.forward(50+50*2**(1/2))
    first=True
    while True:
        print(star.position())
        if first:
            star.left(90) #if we use we are marked octo
            star.forward(50)
            star.pendown()
        else:
            star.left(45) #if we use we are marked octo
            star.forward(step)
        first=False
    

if __name__ == '__main__':
    star=turtle.Turtle()
    step=100
    main(star)
