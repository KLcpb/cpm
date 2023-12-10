'''Для ПО кондитерской фабрики нужно написать родительский класс Candy (Конфеты). Этот класс имеет атрибуты name, price, weight (наименование, цена, вес). Подклассы Chocolate, Gummy, HardCandy (шоколад, жевательный мармелад, леденец) наследуют все атрибуты суперкласса Candy. Кроме того, у них есть и свои атрибуты:

Chocolate – cocoa_percentage (процент содержания какао) и chocolate_type (сорт шоколада).
Gummy – flavor и shape (вкус и форма).
HardCandy – flavor и filled (вкус и начинка).

Реализовать сортировку списка из данных объектов (в списке втсречается как объекты классов Chocolate, Gummy, HardCandy) по цене.
'''

class candy:
    def __init__ (self, name, weight,price):
        if isinstance(weight, int or float) and isinstance(price, int or float) and isinstance(name,str):
            self.name = name
            self.weight = weight
            self.price = price
        else:
            raise ValueError("invalid data type1")
class gummy(candy):
    def __init__ (self, flavor, shape,*args):
        if isinstance(flavor, str) and isinstance(shape, str):
            super().__init__(*args)
            self.flavor = flavor
            self.shape = shape
        else:
            raise ValueError("type error(flavor/shape)")
    def __lt__(self, other):
         return self.price < other.price     
class chocolate(candy):
    def __init__ (self, cocoa_percentage, chocolate_type,*args):
        if cocoa_percentage <= 100 and isinstance(cocoa_percentage, int or float) and isinstance(chocolate_type, str) :
            super().__init__(*args)
            self.cocoa_percentage = cocoa_percentage
            self.chocolate_type = chocolate_type
        else:
            raise ValueError("invalid data type")
    def __lt__(self, other):
         return self.price < other.price     

class hardcandy(candy):
    def __init__ (self, flavor, filled,*args):
        if isinstance(flavor, str) and isinstance(filled, str):
            super().__init__(*args)
            self.flavor = flavor
            self.filled = filled
        else:
            raise ValueError("invalid data type2")
    def __lt__(self, other):
         return self.price < other.price      
a = hardcandy("privet","da","mishka",2,100)
b = gummy("abab","ifis","net",78,56)
c = chocolate(34,"ifis","net",78,233)

lst = [b,a,c]
lst.sort()
print(lst)
