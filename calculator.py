class Calculator:
    def __init__(self, op1:float, op2:float) -> float:
        self.op1 = op1
        self.op2 = op2

    def sum(self):  # a+b
        return self.op1 + self.op2
    def sub(self):  # a-b
        return self.op1 - self.op2
    def mul(self):  # a*b
        return self.op1 * self.op2
    def div(self):  # a/b
        if self.op2 != 0:
            return self.op1 / self.op2

# Przykłady wywołania
'''
calculator = Calculator(5,0)
print(calculator.sum())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())
'''