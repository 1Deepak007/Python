class Employee:
    
    def __init__(self,name):
        self.name=name
        
    def __len__(self):
        i = 0
        for x in self.name:
            i+=1
        return i
        
    def __str__(self):
        return f"name of CEO is {self.name}. str"
    
    
    def __repr__(self):
        return f"name of CEO is {self.name}. repr"

    