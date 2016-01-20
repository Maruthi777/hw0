obj = open ("iowa-liquor-sample.csv","r")
count=0
substring="single malt scotch"
for line in obj:
    lin1=line.lower()
    if substring in lin1:
        count=count+1
print(count)
obj.close()
