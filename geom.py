import math

class Figure():
    __heights = 0
    __list = []
    def __init__(self,lst):
        self.__heights = len(lst)
        self.__list = list(lst)
        
    def info(self):
        print(f"number of heights: {self.__heights}")
        if self.__heights == 3:
            print("its triangle")

    def summa(self,lst):
        P = 0
        for i in range(len(lst)):
            P += math.sqrt((lst[i][0] - lst[i-1][0])**2 + (lst[i][1] - lst[i-1][1])**2 )
        return P
#[[x,y],[x,y]]

class Triangle(Figure):
    #ABC alpa beta gamma
    __A = 0
    __B = 0
    __C = 0
    __lst = []
    
    def __init__(self,lst):
        self.__heights = len(lst)
        if self.__heights != 3:
            print("error creating triangle")
        self.__lst = list(lst)
        self.__A = math.sqrt((lst[1][0] - lst[0][0])**2 + (lst[1][1] - lst[0][1])**2)
        self.__B = math.sqrt((lst[2][0] - lst[1][0])**2 + (lst[2][1] - lst[1][1])**2)
        self.__C = math.sqrt((lst[0][0] - lst[2][0])**2 + (lst[0][1] - lst[2][1])**2)

    def __area__(self):
        p = super().summa(self.__lst)/2
        return round(math.sqrt(p*(p-self.__A)*(p-self.__B)*(p-self.__C)),2)
        
    def info(self):
        print("A B C",round(self.__A,2),round(self.__B,2),round(self.__C,2))
        print("area ",self.__area__())
class Rect(Figure):
    __A = 0
    __B = 0
    __C = 0
    __D = 0
    def __init__(self,lst):
        self.__heights = len(lst)
        if self.__heights != 4:
            print("error creating rectangle")
        self.__lst = list(lst)
        self.__A = math.sqrt((lst[1][0] - lst[0][0])**2 + (lst[1][1] - lst[0][1])**2)
        self.__B = math.sqrt((lst[2][0] - lst[1][0])**2 + (lst[2][1] - lst[1][1])**2)
        self.__C = math.sqrt((lst[3][0] - lst[2][0])**2 + (lst[3][1] - lst[2][1])**2)
        self.__D = math.sqrt((lst[0][0] - lst[3][0])**2 + (lst[0][1] - lst[3][1])**2)
        
    def __area__(self):
        return self.__A * self.__B

    def info(self):
        print("A B C D",round(self.__A,2),round(self.__B,2),round(self.__C,2),round(self.__D,2))
        print("area ",self.__area__())


a = Rect([[0,0],[2,0],[2,2],[0,2]])

a.info()