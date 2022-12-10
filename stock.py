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

    def setPreviousClosingPrice(self, newPreviousClosingPrice):
        if isinstance(newPreviousClosingPrice, int):
            newPreviousClosingPrice = float(newPreviousClosingPrice)
        if isinstance(newPreviousClosingPrice, float) and newPreviousClosingPrice >= 0:
            self.__previousClosingPrice = newPreviousClosingPrice
        else:
            raise ValueError("Setting new Previous Closing Price must be a positive number")
        

    def getCurrentPrice(self):
        return self.__currentPrice


    # SETTER FOR CURRENT PRICE VERY SIMILAR TO PREVIOUS COLSING PRICE

    # GET PERCENT METHOD 

    # FOLLOW TEST EXAMPLE
    
    # COMMENTS
