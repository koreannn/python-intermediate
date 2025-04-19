class Vector(object):
    def __init__(self, *args):
        """
        - Create a vector
        - Example of create vector instance: v = Vector(5, 10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0 # unpacking
        else:
            self._x, self._y = args # unpacking
            
    def __repr__(self):
        """
        Return the vector information
        """
        return "Vector(%r, %r)" % (self._x, self._y)
    
    
    def __add__(self, other: "Vector") -> "Vector":
        """
        Return the vector addition of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)
    
    
    def __mul__(self, mul_num: int) -> "Vector":
        """
        Return the vector multiplication of self and other
        """
        return Vector(self._x * mul_num, self._y * mul_num)
        
        
    def __bool__(self) -> bool:
        """
        Return the vector is zero or not
        """
        return bool(max(self._x, self._y))
        

print(Vector.__doc__) # 클래스에 대한 주석은 없으므로, None
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print()
print()

v1 = Vector(5, 10)
v2 = Vector(10, 20)
v3 = Vector() # 예외처리로 인해 에러가 발생하지 않음

print(v1, v2, v3) # __repr__
print(v1+v2) # __add__
print(v1*3) # __mul__
print(bool(v1), bool(v2), bool(v3)) # __bool__

print()
print()

if bool(v1): # 영벡터일경우 False, 영벡터가 아닐경우 True
    print("ok")
