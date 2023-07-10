class node:
    def __init__(self,data):
        self.data=data
        self.next1=None # foir crewating a data part ansd addres
class ll:
    def __init__(self):
        self.head=None
    def new(self,newval):
        f=node(newval)
        f.next1=self.head
        self.head=f
    def hi(self):
        b=self.head       #for creating a node
        while b is not None:
            print(b.data,end="->>")
            b=b.next1
a=ll()
a.head=node("mon")    #assignig values
e2=node("tue")
e3=node("thur")
a.head.next1=e2     # connectibg link bw to nodes
e2.next1=e3
a.new("sun")

a.hi()               # a m,ethod for printing
