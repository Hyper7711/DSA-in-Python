class Test:  # creating the class
    x = 5  # class object variable
         
    def f1(self):
        print(self.x)
                    
        
t1 = Test()  # instance object
t2 = Test()  # instance object
t1.f1()
t2.f1()
print(t1.x, t2.x)


class ABC:
            
    def __init__(self):
        # remember: Only a =local variable / 'self.a'=inst obj var
        self.a = 5  # inst obj var
        self.b = 6  # inst obj var


t3 = ABC()
t4 = ABC()

print(t3.a, t3.b)
print(t4.a, t4.b)


class pqr:
   
    def __init__(self, c, d):
        self.c = c
        self.d = d
        
    def show(self):  # method
        print(self.c, self.d)
        
    @staticmethod
    def f2():  # static method to create obj
        pass
   
    @classmethod
    def f3(cls):  # class method to create obj
        pass
     

t5 = pqr(7, 8)
t6 = pqr(9, 10)

print(t5.c, t5.d)
print(t6.c, t6.d)

t5.show()
t6.show()
