print("type of int: ", int)
print("type of float: ", float)
n = 10
print("type of n: ", type(n))

print()
print()

print("dir of int type: ", dir(int))
print("dir of float type: ", dir(float))
print("dir of n type: ", dir(n))

print()
print()

print(n+100)
print(n.__add__(100))

"""매직 메서드의 오버라이딩"""
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    # 오버라이딩1. 인스턴스의 출력
    def __str__(self):
        return "Fruit Class Info: {}, {}".format(self._name, self._price)
    
    def __add__(self, x):
        print("Called >> __add__")
        return self._price + x._price
    
    def __sub__(self, x):
        print("Called >> __sub__")
        return self._price - x._price
        
    def __le__(self, x):
        print("Called >> __le__")
        if self._price <= x._price:
            return True
        else:
            return False
    
    def __ge__(self, x):
        print("Called >> __ge__")
        if self._price >= x._price:
            return True
        else:
            return False
    
    def __eq__(self, x):
        print("Called >> __eq__")
        return self._price == x._price
        
# 인스턴스 생성
f1 = Fruit("Watermelon", 7500)
f2 = Fruit("Banana", 3000)

print(f1._price + f2._price) # 지양해야하는 방식 (인스턴스 변수가 직접적으로 노출되는 방식)
print(f1+f2)
print(f1-f2)
print(f1<=f2)
print(f1>=f2)