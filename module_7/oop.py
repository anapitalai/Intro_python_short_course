
# Example: Creating a class for a basic car 
class Car: def __init__(self, make, model):
 self.make = make self.model = model def start_engine(self): 
return f"{self.make} {self.model}'s engine is running." 
# Creating objects 
car1 = Car('Toyota', 'Camry') car2 = Car('Honda', 'Accord') 
# Using methods 
print(car1.start_engine()) 
print(car2.start_engine())



# Create a Friend Class that shows the name, sex and age of your friend!
class Student():
    """Show simple information about a student."""
    def __init__(self, name, id, department):
        # Attributes of your friend
        self.name = name
        self.id = id
        self.department = department 
        
    def describe(self):
        # Describe the characteristics of the student
        print("The student’s name is ", self.name, " having an ID of ", self.id, "from the ", self.department ".")


# Create class of your first friend
student1 = Student('Alois Napitala', '2309007.3', 'Survey and lands Studies')


