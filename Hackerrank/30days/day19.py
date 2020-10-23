class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        li = []
        for i in range(n + 1):
            try:
                if (n % i == 0):
                    li.append(i)
            except ZeroDivisionError:
                pass
        return sum(li)



n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)