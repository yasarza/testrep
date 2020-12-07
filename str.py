class String:
    def __init__(self,value = None):
        self.__value = value

    def __str__(self):
        return str(self.__value)

    
x = String(2)
print(x)