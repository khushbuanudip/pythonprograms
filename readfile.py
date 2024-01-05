f=open("demofile.txt","r")
count=0
count1 = 0
for x in f:
    print(x)
    words=x.split()
    for word in words:
      count1 = count1 + 1 
      count=count+1
    print("no of words line by line",count1)
    count1=0
print("no of words in file",count)
