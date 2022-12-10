class Stock:
    """ represents a company's stock """
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def __str__(self):
        return f"Symbol: {self.__symbol},  Name: {self.__name},  Previous Closing Price: {self.__previousClosingPrice},  Current Price: {self.__currentPrice}"

    def getSymbol(self):
        return self.__symbol

    def getName(self):
        return self.__name

    def getPreviousClosingPrice(self):
        return self.__previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice