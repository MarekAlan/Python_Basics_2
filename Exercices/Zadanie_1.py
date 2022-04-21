class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        self.history.append(f'{num1} + {num2} = {num1+num2}')
        return num1 + num2

    def multiply(self, num1, num2):
        self.history.append(f'{num1} * {num2} = {num1 * num2}')
        return num1 * num2

    def print_operations(self):
        for op in self.history:
            print(op)

parzyste = Calculator()
pierwsze = Calculator()

print(parzyste.add(4, 8))
print(parzyste.add(100, 200))
print(parzyste.multiply(10, 16))
print(pierwsze.add(13, 17))
print(pierwsze.multiply(23, 29))

print('Parzyste: ')
parzyste.print_operations()
print('Pierwsze: ')
pierwsze.print_operations()