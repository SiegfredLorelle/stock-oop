from stock import Stock

a = Stock("INTC", "Intel Corporation", 20.5, 20.35)
print(a.getSymbol())
print(a.getName())
print(a.getPreviousClosingPrice())
print(a.getCurrentPrice())