class Car:
    def __init__(self, brand, model, color, onSale, marketPrice, sellingPrice, kmPerLiter, reperationer):
        self.brand = brand
        self.model = model
        self.color = color
        self.onSale = onSale
        self.marketPrice = marketPrice
        self.sellingPrice = sellingPrice
        self.kmPerLiter = kmPerLiter
        self.reperationer = reperationer

    def calculateSalesBonus(self):
        salesBonus = int((self.marketPrice - self.sellingPrice) * 0.20)
        try:
            if salesBonus >= 2000 and salesBonus <= 5000:
                extraBonus = salesBonus + 500
                return extraBonus
            elif salesBonus <= 2000:
                extraBonus = salesBonus + 1000
                return extraBonus
            elif salesBonus >= 5000:
                salesBonus = 5000
                return salesBonus
            else:
                salesBonus = 0
                return salesBonus
        except:
            return 'Noget gik galt.'
