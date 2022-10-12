def main(step:int)->int:
    stepx=8000
    for i in range(step):
        if i==0:
            # stepx=8000
            continue
        else:
            stepx+=stepx*increase
    return stepx

if __name__ == '__main__':
    increase=3/100
    step=int(input("calculate years"))
    returnx=main(step)

    print("calculate {b} for {a}".format(a=step,b=returnx))