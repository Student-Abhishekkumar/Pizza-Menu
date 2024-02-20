def menu():
    print("\n........WELCOME! TO CORNOR PIZZA........")
    print("\n    Which size of pizza you want ?")
    print("\n\t 1. Small")
    print("\t 2. Medium")
    print("\t 3. Large")

while True:
    menu()
    bill=0.0
    choice=int(input("\nEnter your choice : "))
    if(choice==1):
        bill+=100
        ask=input("\nDo you want pepperoni (y/n) : ")
        if(ask=='y'):
            bill+=30
            ask2=input("\nDo you want extra cheese (y/n) : ")
            if(ask2=='y'):
                bill+=20
                print("\nTotal Bill - Rs",bill)
                break
            elif(ask2=='n'):
                print("\nTotal Bill - Rs",bill)
                break
        elif(ask=='n'):
            ask2=input("\nDo you want extra cheese (y/n) : ")
            if(ask2=='y'):
                bill+=20
                print("\nTotal Bill - Rs",bill)
                break
            elif(ask2=='n'):
                print("\nTotal Bill - Rs",bill)
                break
            else:
                print("INVALID CODE.....")
                continue
        else:
            print("INVALID CODE.....")
            continue
    elif(choice==2):
        bill+=200
        ask=input("\nDo you want pepperoni (y/n) : ")
        if(ask=='y'):
            bill+=30
            ask2=input("\nDo you want extra cheese (y/n) : ")
            if(ask2=='y'):
                bill+=20
                print("\nTotal Bill - Rs",bill)
                break
            elif(ask2=='n'):
                print("\nTotal Bill - Rs",bill)
                break
        elif(ask=='n'):
            ask2=input("\nDo you want extra cheese (y/n) : ")
            if(ask2=='y'):
                bill+=20
                print("\nTotal Bill - Rs",bill)
                break
            elif(ask2=='n'):
                print("\nTotal Bill - Rs",bill)
                break
            else:
                print("INVALID CODE.....")
                continue
        else:
            print("INVALID CODE.....")
            continue
    elif(choice==3):
        bill+=300
        ask=input("\nDo you want pepperoni (y/n) : ")
        if(ask=='y'):
            bill+=30
            ask2=input("\nDo you want extra cheese (y/n) : ")
            if(ask2=='y'):
                bill+=20
                print("\nTotal Bill - Rs",bill)
                break
            elif(ask2=='n'):
                print("\nTotal Bill - Rs",bill)
                break
        elif(ask=='n'):
            ask2=input("\nDo you want extra cheese (y/n) : ")
            if(ask2=='y'):
                bill+=20
                print("\nTotal Bill - Rs",bill)
                break
            elif(ask2=='n'):
                print("\nTotal Bill - Rs",bill)
                break
            else:
                print("INVALID CODE.....")
                continue
        else:
            print("INVALID CODE.....")
            continue
    else:
        print("INVALID CODE.....")
        continue