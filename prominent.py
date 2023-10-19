from thisclass import ThisClass
from thatclass import ThatClass

class Prominent:

    @staticmethod
    def find(self):                              
        return  self.print_something()
    
thisclass = ThisClass()
thatclass = ThatClass()
prominent =Prominent()
prominent.find(thisclass)
prominent.find(ThisClass())
prominent.find(thatclass)
prominent.find(ThatClass())