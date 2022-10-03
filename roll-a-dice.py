import random
response="y"
a=1
while a==1:
    while response=="y":
        n=random.randint(1,6)
        if n==1:
            print("[     ]\n[  0  ]\n[     ]")
        if n==2:
            print("[     ]\n[ 0 0 ]\n[     ]")
        if n==3:
            print("[     ]\n[0 0 0]\n[     ]")
        if n==4:
            print("[0   0]\n[     ]\n[0   0]")
        if n==5:
            print("[0   0]\n[  0  ]\n[0   0]")
        if n==6:
            print("[0   0]\n[0   0]\n[0   0]")
        response="n"
    response=input("Press 'y' to cont., 'n' to exit- ")
    print("\n")