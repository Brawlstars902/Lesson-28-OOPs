import time
class Employee:
    def __init__(self,name):
        self.name=name
        print('Employee Created: ',name)

    def __del__(self):
        print('Destructer called\nDeleting Class: Employee...')
        print('Class Terminated')
    
def create(obj):
    print('Creating object...')
    obj=Employee(str(obj))
    print('Object created. Name: ',obj.name)

print('Using create function')
create('Bob')

