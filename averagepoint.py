import csv
file = open('data.csv',encoding="utf8")
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)
rows = []

for row in csvreader:
        rows.append(row)
        

        
        
dataA=[]
dataB=[]
dataC=[]
dataD=[]
dataE=[]
dataF=[]
dataG=[]
dataH=[]
dataI=[]
for i in rows:
        if i[0]=="PointA":
                dataA.append(i[2])
        elif i[0]=="PointB":
                dataB.append(i[2])
        elif i[0]=="PointC":
                dataC.append(i[2])
                
print(dataA) 
sumA=0
avgA=0
for i in dataA:
        sumA += float(i)
avgA=sumA/len(dataA)
print(avgA)
finaldata=[]
finaldata.append(avgA)
print(finaldata)


'''elif i[0]=="PointB":
                dataB.append(i[2])
        elif i[0]=="PointC":
                dataC.append(i[2])
        elif i[0]=="PointD":
                dataD.append(i[2])
        elif i[0]=="PointE":
                dataE.append(i[2])
        elif i[0]=="PointF":
                dataF.append(i[2])
                
        elif i[0]=="PointG":
                dataG.append(i[2])
        elif i[0]=="PointH":
                dataH.append(i[2])
        elif i[0]=="PointI":
                dataI.append(i[2])'''
        
