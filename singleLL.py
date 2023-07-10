class node:
    def __init__(self,data):
        self.data=data   # foir crewating a data part ansd addres
        self.next1=None
        self.data1=data   # foir crewating a data part ansd addres
        self.next11=None
class ll:
    def __init__(self):
        self.head1=None
        self.head=None
    def hi(self):
        b=self.head#for creating a node
        d=self.head1
        
        a=0
        while b and d is not None:
           a=b.data+d.data1
           print(a,end=' ')
           b=b.next1
           d=d.next11
a=ll()
a.head=node(1)    #assignig values
e2=node(2)
e3=node(3)
e4=node(4)
a.head1=node(1)    #assignig values
e9=node(2)
e8=node(3)
e7=node(4)
a.head.next1=e2     # connectibg link bw to nodes
e2.next1=e3
e3.next1=e4
a.head1.next11=e9     # connectibg link bw to nodes
e9.next11=e8
e8.next11=e7
a.hi()               # a m,ethod for printing
