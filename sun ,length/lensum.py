list1=[1,3,5,7,9,11,34]
list2=[5,13,45,7,20,65,1]
s=int(0)
c=int(0)
for i in list1 and list2:
    if (len(list1)==len(list2)):
        print("list are same length")
        break
    else:
        print("list has different length")
        break
for i in range(0,len(list1)and len(list2)):
    s=s+list1[i]
    c=c+list2[i]
for i in range(0,len(list1)and len(list2)):
    if(s==c):
        print("sum of values are same")
        break
    else:
        print("sum of values are different")
        break
print("elements that matched are:")
l=[]
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if(list1[i]==list2[j]):
            l.append(list1[i] and list2[j])
        else:
            p=i
            continue
print(l)
