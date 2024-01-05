menu={'tea':10,'coffee':20,'iced tea':30,'green tea':40,'black tea':50}
quantity={'tea':0,'coffee':0,'iced tea':0,'green tea':0,'black tea':0}
sum=0

print(menu)
l1=[]
a=int(input("Enter number of items to be ordered"))

if a<=4:
 for i in range(1,a+1):   
  b=input("Enter item name to be ordered")
  l1.append(b)

for val in l1:
    quantity[val]=quantity[val]+1
    sum=sum+menu[val]

print("Order Item:Quantity",quantity)
print("Total Amount:",sum)  

