class Parser:
    def validate(self, value):
        if '.' in value:
            return float(value)
        return int(value)

    def convert(self, expresion):
        a, op, b = tuple(str.split(expresion))
        return self.validate(a), self.validate(b), op

class Core:
    def __init__(self):
        self.parser = Parser()
        self.functions = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b
        }

    def calculate(self, expression):
        a, b, op = self.parser.convert(expression)        
        return self.functions.get(op)(a, b)

class Interface:
    def __init__(self):
        self.core = Core()
    
    def run(self):
        while True:
            print('Enter your expression')
            expresion = input()
            result = self.core.calculate(expresion)
            print('Result is {}'.format(result))
            print('=' * 15)

if __name__ == '__main__':
    calculator = Interface()
    calculator.run()

