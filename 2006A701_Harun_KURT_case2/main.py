
from instant_patient import InstantPatient
from regular_patient import RegularPatient
from patient import Patient


from typing import List, TypeVar,NewType

def main():
    selected=int()
    
    while selected>(-1):
        print(printed)
        selected=int(input(" Selected : "))
        if selected==0:
            continue           
        elif selected ==1 :
            
            first_name=str(input("Input first_name : "))
            last_name=str(input("Input last_name : "))
            healtcare_security=str(input("Input healtcare_security[SGK,Yeşil_kart,Yok] : "))
            regular_patient=int(input("Input Regular Patient Press(1) : "))
            no_key=False
            # while no_key!=True:
            
            if regular_patient==1 :
                patient_list.append(
                 RegularPatient(
                    first_name,
                    last_name,
                    healtcare_security,
                    )
                )
            else :
                payment = int(input("Payment : "))
                hour = int(input("Hour :  "))
                patient_list.append(
                 InstantPatient(
                    first_name,
                    last_name,
                    healtcare_security,
                    hours=hour,
                    payment_per_hour=payment
                    ) 
                )
                
        elif selected==2:
            for itemPatient in patient_list:
                print(itemPatient,itemPatient.calculate_cost())
                

if __name__ == '__main__':
    printed="""
    Hastaneye Yeni bir hasta eklemek istiyorsanız 1 seçiniz,
    Hastaları listemek için 2,
    Menüye dönmek için 0'a basınız,
    çıkmak için -1 tuşlayınız.
    """
    
    try:
        p = Patient("aa", "ss", "SGK")
    except TypeError as e:
        print(e)

    patient_list=list()
    print(patient_list)
    patient_list.append(RegularPatient("Ahmet","B","SGK",200))
    patient_list.append(RegularPatient("Mehmet","B","SGK",100))
    patient_list.append(RegularPatient("Yahya","B","SGK",500))
    patient_list.append(InstantPatient("Harun","B","SGK",55,70))
    print(patient_list)
    main()
    