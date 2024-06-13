a=[7,1,5,2,6]
for i in range(1,len(a)):
    j=i
    while j>0:
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
            
        j=j-1
print(a)
#comment
