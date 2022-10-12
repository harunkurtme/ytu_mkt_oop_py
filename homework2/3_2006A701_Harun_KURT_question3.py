def main(step:int)->float:
    sleep=0
    for i in range(step):
        sleep+=float(input("{a}. day how much hour sleep ?".format(a=i+1)))
    return sleep/7
if __name__ == '__main__':
    # increase=3/100
    step=7 #daty
    returnx=main(step)

    print("sleep 7 day avarge hour sleep {b}".format(b=returnx))