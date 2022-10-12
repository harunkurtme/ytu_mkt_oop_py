#daiyly 


start_number=float(input("first population organism"))
increase=float(input("population increase with %100"))/100

for i in range(10):
    if i == 0:
        start_number+=start_number*increase*0
    else :
        start_number+=start_number*increase


    print("{0}. day increase organism {1} ".format(i+1,start_number))