class Friend():
    """This class describes the name, sex and age of my friend."""
    def __init__(self, name, sex, age):
        # Attributes of your friend
        self.name = name
        self.sex = sex
        self.age = age
    
        
    def describe(self):
        # Describe to a person your friend's characteristics
        print("My best friend is: ", "\nName: ", self.name, "\nSex: ", self.sex, "\nAge: ", self.age)
        
friend2 = Friend('Jonathan', 'Male', 25)
friend2.describe()
        
##Instance of Friend

friend=Friend('Alois','Male','43')

print(friend.describe())
print(friend.name)
        
