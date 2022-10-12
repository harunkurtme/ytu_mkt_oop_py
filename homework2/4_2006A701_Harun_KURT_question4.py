import turtle
import fractions

def main(step:int)->int:
    stepx=1
    for i in range(step):
        if i==0:
            i=1
        stepx*=i
    return stepx

if __name__ == '__main__':
    step=int(input("calculate factorial"))
    returnx=main(step)

    print("calculate {b} for {a}".format(a=step,b=returnx))