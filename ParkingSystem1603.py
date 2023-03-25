# 設計一個停車系統，停車場有三種停車位大小：大、中、小，每種大小的停車位都有固定數量的車位。
# 初始化 ParkingSystem 類的對象。每種大小的停車位數量作為構造函數的一部分給出。
# bool addCar(int carType)：檢查是否有對應車型的停車位可供想要進入停車場的車輛使用。車型分為三種：大、中、小，分別由 1、2、3 表示。
#　車輛只能停放在與其車型對應的停車位上。如果沒有可用的空間，返回 false，否則在該大小的停車位上停車，並返回 true。
# 將傳入的三個整數參數 big、medium、small 分別賦值給了類的屬性 self.big、self.med、self.small，
# 這樣該類的其他方法就可以使用這些屬性來表示停車場中不同大小的停車位的數量。
# 接受一個整數參數 carType，代表車輛的類型，其中 1、2、3 分別表示大型、中型和小型車輛。
# 如果該車型的停車位已經全部被佔用，則返回 False；否則，在該大小的停車位上停車，並返回 True。
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.med = medium
        self.small = small
        
    def addCar(self, carType: int) -> bool:
        self.cartype = carType
        if(self.cartype == 1 and self.big <= 0) or (self.cartype == 2 and self.med <= 0) or (self.cartype == 3 and self.small <= 0):
            return False
        elif self.cartype == 1 and self.big > 0:
            self.big -= 1
            return True
        elif self.cartype == 2 and self.med > 0:
            self.med -= 1
            return True
        elif self.cartype == 3 and self.small > 0:
            self.small -= 1
            return True