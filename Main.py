class Func:
    def loopCalc(self):
        equation = str(input("Equation: "))
        split = equation.split(" ")
        counter = 0
        total = float(0)
        symbol = 0
        total = int(split[0])
        for x in split[1:len(split)]:
            if x.isnumeric() == True:
                symbol, total = Filter.numberFilter(0, symbol, total, int(x))
            elif x in ("+-//**"):
                symbol = Filter.symbolFilter(0, x)
        print(f"{equation} = {total}")


class Filter():
    def numberFilter(self, symbol, total, x):
        if not(symbol == 0):
            if symbol == 1:
                total += x
            elif symbol == 2:
                total /= x
            elif symbol == 3:
                total *= x
            elif symbol == 4:
                total -= x
            elif symbol == 5:
                total **= x
            elif symbol == 6:
                total //= x
        return 0, total

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
        elif x == "//":
            symbol = 6
        return symbol
if __name__ == "__main__":
    Func.loopCalc(0)
