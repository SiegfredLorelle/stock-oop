class Stock:
    """ Represents a company's stock """
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        """ Initialize attributes of the stock as private without default values (as instructed in the pdf) """
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def __str__(self):
        """ If the object/stock is printed out, print the attributes of the object/stock """
        return f"Symbol: {self.__symbol},  Name: {self.__name},  Previous Closing Price: {self.__previousClosingPrice},  Current Price: {self.__currentPrice}"

    # Symbol attribute getter
    def getSymbol(self):
        """ Returns the symbol of the stock """
        return self.__symbol

    # Name attribute setter
    def getName(self):
        """ Returns the name of the stock """
        return self.__name

    # Previous CLosing Price getter
    def getPreviousClosingPrice(self):
        """ Returns the previous closing price of the stock """
        return self.__previousClosingPrice

    # Previous Closing price setter
    def setPreviousClosingPrice(self, newPreviousClosingPrice):
        """ Set a new previous closing price if it is valid """
        # If the given previous closing price is an int, then convert it to float
        if isinstance(newPreviousClosingPrice, int):
            newPreviousClosingPrice = float(newPreviousClosingPrice)
        
        # If the given previous closing price is valid (a non negative float), then set it as the previous closing price of the stock
        if isinstance(newPreviousClosingPrice, float) and newPreviousClosingPrice >= 0:
            self.__previousClosingPrice = newPreviousClosingPrice

        # If the given current price is invalid, call an error
        else:
            raise ValueError("Setting new Previous Closing Price must be a positive number")

    # Current Price getter
    def getCurrentPrice(self):
        """ Returns the current price of the stock """
        return self.__currentPrice

    # Current Price setter
    def setCurrentPrice(self, newCurrentPrice):
        """ Set a new current price if it is valid """
        # If the given current price is an int, convert it to float
        if isinstance(newCurrentPrice, int):
            newCurrentPrice = float(newCurrentPrice)

        # If the given current price is valid (non negative float), then set it as the current price of the stock
        if isinstance(newCurrentPrice, float) and newCurrentPrice >= 0:
            self.__currentPrice = newCurrentPrice

        # If the given current price is invalid, call an error
        else:
            raise ValueError("Setting new Current Price must be a positive number")


    def getChangePercent(self):
        """ Returns the percentage change from previous closing price to current price """
        return ( (self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice ) * 100



# TEST (suggest using the uploaded test.py for testing)
def main():
    # Create a stock for intel
    intelStock = Stock("INTC", "Intel Corporation", 20.5, 20.35)

    # # UNCOMMENT TO SET A DIFFERENT CLOSING PRICE AND CURRENT PRICE
    # a.setPreviousClosingPrice(20.5)
    # a.setCurrentPrice(20.35)
    
    # Print out the price change percentage of intel from previous closing price to current price
    print(f"The price-change percentage of {intelStock.getName()}'s ({intelStock.getSymbol()}) stock is {intelStock.getChangePercent():,.2f}%")


if __name__ == "__main__":
    main()