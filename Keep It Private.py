class myClass:
    
    __privateVar = 27
    
    def __privMeth(self):
        print("I am Inside Class 'myClass' and 'privmeth' Method")
    
    def hello(self):
        print(f"Private Variable Value:", myClass.__privateVar) 
        
foo = myClass()
foo.hello()
foo.__privMeth()