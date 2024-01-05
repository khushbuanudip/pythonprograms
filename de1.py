import constant

#x=int(input("enter any value"))
#print(x)
#print(type(x))
#y=int(input("enter value of y"))
#print(x+y)
#x=5
#y="9"
#print(x+int(y))


print("|{:<30}|{:^10}|{:>10}|".format("butter","bread", "jam"))

r=int(input("Enter the value of radius"))
h=float(input("enter the value of height"))
Volume=constant.PI*r*r*h
print(Volume)
print('volume of cyllinder is{0:.2f} and its radius is {1}'.format(Volume,r))
exp="Exponent representation: {0:e}".format(1566.345)
print(exp)
print("One third is: {0:.4f}".format(1/3))
print("|{:<30}|{:^10}{:>20}|".format("butter","butter","bread")
