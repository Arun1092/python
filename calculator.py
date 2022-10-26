from pickle import TRUE


a=int(input("enter a number"))
b=int(input("enter the second number"))
while TRUE:
    print("main menu\n")
    print("1 addition")
    print("2 substration")
    print("3 multiplication")
    print("4 division")
    print("5 exit")
    choice=int(input("enter your choice"))
    if choice==1:
        sum=a+b
        print("sum=",sum)
    elif choice==2:
        sub=a-b
        print("sub=",sub)

    elif choice==3:
        mul=a*b
        print("mul=",mul)
    elif choice==4:
        div=a/b
        print("div=",div)
    elif choice==5:
        break       
    else:
        print("enter the correct choice")