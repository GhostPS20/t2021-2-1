class Calculator:
    def __init__(self, a, b, op):
        self.a = a
        self.b = b
        self.op = op

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b



a = float(input())
b = float(input())
op = input()
result=None

c = Calculator(a, b, op)

if op == "+":
    result = c.addition()
elif op == "-":
    result = c.subtraction()
elif op == "*":
    result = c.multiplication()
elif op == "/":
    result = c.division()
else:
    print("Invalid operator")

print(result)
