class OP:
    def arithematic(a,b):
        print("addition:",a+b)
        print("Division:",a/b)
    def assignment(a):
        print ("assignment:",a>=1)
    def comparison(a,b):
        print ("comparison:",a>b)
    def logical(a,b):
        print("Logical:",a>b or a<b)
    def identity(a,b):
        print ("identity:", a is b)
    def membership():
        a="yash is my"
        b="is"
        print ("Memebership:",a in b)
    def bitwise(a,b):
        print("Bitwise &:",a&b)
obj=OP()
OP.arithematic(20,43)
OP.assignment(23)
OP.comparison(54,76)
OP.logical(12,76)
OP.identity(23,23)
OP.membership()
OP.bitwise(23,54)
    
        
