from secrets import choice


cars=["ford","bmw","safari","ferrari","tata"]
while True:
    print("\n main menu")
    print("1 append to the array")
    print("2 remove from the array")
    print("3 exit")
    choice=int(input("enter your choice"))
    if choice==1:
        num=int(input("how many car  you want to append"))
        for i in range(num):
            newcar=input("enter the new car name")
            cars.append(newcar)
        for i in cars:
            print(i)
    elif choice==2:
        print("removing")
        rem=input("enter the car to be removed")
        cars.remove(rem)
        for i in cars:
            print(i)
    elif choice==3:
        break
    else:
        print("sorry incorrect choice")
