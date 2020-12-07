class Circle:
    def __init__(self,radius = 0):
        self.__radius = radius
    def setRadius(self):
        value = float(input('Enter the circle radius: '))
        if value >= 0:
            self.__radius = value
        else:
            raise ValueError('this value should be a positive vale!')
    
    def calacArea(self):
        return float((self.__radius ** 2 )  * 3.14159)

class Circle2:
    def __init__(self,radius):
        self.__radius = radius
    def __setRadius(self,value):
        if value >= 0:
            self.__radius = value
        else:
            raise ValueError('this value should be a positive vale!')
        
    radius = property(None, __setRadius)


    @property
    def calacArea(self):
        return float((self.__radius ** 2 )  * 3.14159)



circleOne = Circle()
circleOne.setRadius()
print(type(circleOne.calacArea()))
circleTwo = Circle2(23)
print(type(circleTwo.calacArea))
