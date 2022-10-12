
from re import S


def main(step:int)->int:
    stepx=0
    for i in range(step):
        if i==0:
            stepx=increase_mm
        else:
            stepx+=increase_mm*i
    return stepx

if __name__ == '__main__':
    increase_mm=16/1000
    step=int(input("calculate years"))
    returnx=main(step)

    print("calculate {b} for {a}".format(a=step,b=returnx))