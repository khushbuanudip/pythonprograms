list1=[3,76,34,98,45]
list1.append(33)
print(list1)
max1=list1[0]
temp = 0
for no in range(1,len(list1)):
    print(no)
    if ( max1 > list1[no]):
        temp= list1[no-1]
        list1[no-1] = list1[no]
        list1[no] = temp
    else:
        max1=list1[no]
print(list1)
