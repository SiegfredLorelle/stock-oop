from stock import Stock
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