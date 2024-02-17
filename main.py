dic={1:"ponedelnik",2:"vtornik",3:"sreda",4:"4etverg",5:"pyatniza-razvrantica",6:"sb",7:"vs"}

class Week():
    days = []
    def __init__(self,*args):
        if not args[0]==None:
            for arg in args:
                self.days.append(arg)

    def __repr__(self):
        s = ''
        for i in self.days:
            s+=str(i)
        return s

class Day():
    def __init__(self, date, *args):
        self.lessons=[]
        self.date = date
        for arg in args:
            self.lessons.append(arg)

    def __repr__(self):
        s = ''
        s+="DATE "+str(self.date)+f" {dic[self.date%7]}\n"
        for i in self.lessons:
            s+=str(i)+"\n"
        s+="------\n"
        return s
       
class Lesson():
    name=''
    def __init__(self,time,cab,name):
        self.name = name
        self.cab = cab
        self.time=time
        
    def __repr__(self):
        s = self.name + " time-> "+str(self.time) + " cab-> "+str(self.cab) + "\n"
        return s

phys= Lesson(1231,31,'phys')
math = Lesson(1451,301,'math')
litr= Lesson(1231,31,'literatuea')
pe = Lesson(1451,301,'phizra')
prog= Lesson(1231,31,'programminf')
bio = Lesson(1451,301,'biology')

mon = Day(15,math,phys)
tue=Day(16,litr,pe,math)
sr=Day(17,math,math,math)
cht=Day(18,bio,math,math)
pt=Day(19,prog,math,prog)

c=Week(mon,tue,sr,cht,pt)
print(c)
