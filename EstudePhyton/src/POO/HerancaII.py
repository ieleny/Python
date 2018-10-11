class A():
    def __init__(self):
        print("INIT A")
        super().__init__()
    
class B(A):
    def __init__(self):
        print("INIT B")
        super().__init__()
    
class C(A, B):
    def __init__(self):
        print("INIT C")
        super().__init__()
        
C()