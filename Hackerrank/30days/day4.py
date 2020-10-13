class Person:
    def __init__(self, initialAge):
        if (initialAge > 0):
            self.age = initialAge
        else:
            print('Age is not valid, setting it to 0.')

    def amIOld(self):
        if self.age >= 18:
            print('You are old.')
        elif self.age >= 13:
            print('You are a teenager.')
        else:
            print('You are young.')

    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")
        
