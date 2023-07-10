def a(li):
    if len(li)>1:
        la=li[:len(li)//2]
        lr=li[len(li)//2:]
        a(la)
        a(lr)
        i,j,k=0,0,0
        while i<len(la) and j<len(lr):
            if la[i]<lr[j]:
                li[k]=la[i]
                i=i+1
            else:
                li[k]=lr[j]
                j=j+1
            k=k+1
        while i<len(la):
            li[k]=la[i]
            i=i+1
            k=k+1
        while j<len(lr):
            li[k]=lr[j]
            j=j+1
            k=k+1
    return li
        
l1=[1,5,2,7,3,4,78]
b=a(l1)
print(b)

            
