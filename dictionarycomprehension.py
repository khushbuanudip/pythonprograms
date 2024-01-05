square_dict=dict()
for i in range(1,16):
    square_dict[i]=i*i
#print(square_dict)
    

square_dict={num:num*num for num in range(1,16) if num%2==0}
print(square_dict)

old_price={"milk":1.02,"cofee":2.5}
dollar_to_pound=0.76
new_price={key:value*dollar_to_pound for(key,value) in old_price.items()}
#print(new_price)
#print(square_dict)

dict1={"gfg":4,"is":5}
list1=[8,4]
list2=[1,2]
k=zip(list1,list2)
print('k',list(k))
rs={idx:{key:dict1[key] }for(idx,key) in zip(list1,dict1)}
print(rs)
