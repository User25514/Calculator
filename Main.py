class Func:
    def loopCalc(self, equation):
        split = equation.split(" ")
        counter = 0
        total = float(0)
        symbol = 0
        total = int(split[0])
        for x in split[1:len(split)]:
            if x.isnumeric() == True:
                symbol, total = Filter.numberFilter(0, symbol, total, x)
            elif x in ("+-/**"):
                symbol = Filter.symbolFilter(0, x)
        messages.Total(0, equation, total)

    def pluss(self, total, x):
        return total + int(x)

    def divide(self, total, x):
        return total / int(x)

    def times(self, total, x):
        return total * int(x)

    def subtract(self, total, x):
        return total - int(x)

    def power(self, total, x):
        return total ** int(x)


class Filter():
    def numberFilter(self, symbol, total, x):
        if not(symbol == 0):
            if symbol == 1:
                total = Func.pluss(0, total, x)
                symbol = 0
            elif symbol == 2:
                total = Func.divide(0, total, x)
                symbol = 0
            elif symbol == 3:
                total = Func.times(0, total, x)
                symbol = 0
            elif symbol == 4:
                total = Func.subtract(0, total, x)
                symbol = 0
            elif symbol == 5:
                total = Func.power(0, total, x)
                symbol = 0
        return symbol, total

    def symbolFilter(self, x):
        if x == "+":
            symbol = 1
        elif x == "/":
            symbol = 2
        elif x == "*":
            symbol = 3
        elif x == "-":
            symbol = 4
        elif x == "**":
            symbol = 5
        return symbol


class messages():
    def Total(self, equation, total):
        print(f"{equation} = {total}")


equation = str(input("Equation: "))
Func.loopCalc(0, equation)
