def pos(list1,s,st):
    pivot=list1[s]
    i=s+1
    j=st
    
    while True:
        while list1[i]<=pivot and i<=j:
            i=i+1
        while list1[j]>=pivot and i<=j:
            j=j-1
        if i<=j:
            list1[i],list1[j]=list1[j],list1[i]
        else:
            break
            
    list1[j],list1[s]=list1[s],list1[j]
def quick(list1,s,st):
    if s>=st:
        return
    else:
        k=pos(list1,s,st)
        quick(list1,s, k-1)
        quick(list1, k+1,st)
list1=[6,5,2,33,11]
b=len(list1)-1
g=quick(list1,0,len(list1)-1)
print(g)
print(list1)
        
            
