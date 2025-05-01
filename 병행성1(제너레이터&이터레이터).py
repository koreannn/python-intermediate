"""
- 병행성(Concurrency), 흐름 제어
- Iterator
- Generator
- __iter__, __next__
- 클래스 기반으로 제너레이터 구현하기
"""

"""Iterable객체가 반복 가능한 이유"""
t = "ASDFGHJKL"
print(dir(t))

for char in t:
    print(char)

w = iter(t)
print("w: ", w)
print("dir(w): ", dir(w))
print("w.__next__(): ", w.__next__())
print("w.__next__(): ", w.__next__()) # 이 때 중요한건 위치 정보를 기억하고있다는 것

while True:
    try:
        print(next(w))
    except StopIteration:
        break
    
print()

# 반복형 확인
# 1. dir
print("dir(t): ", dir(t))

# 2. hasattr
print("hasattr(t, '__iter__'): ", hasattr(t, "__iter__")) # "t객체가 __iter__ 속성을 가지고 있음?"

# 3. isinstance
from collections import abc # abstract base class (추상 클래스)
print("isinstance(t, abc.Iterable): ", isinstance(t, abc.Iterable)) # "t객체가 abc.Iterable 클래스의 인스턴스임?"

print()
print()


"""클래스로 제너레이터 구현하기"""
# 1. Next Pattern
class WordSplitIterator:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")
        
    def __next__(self):
        print("Called __next__")
        try:
            word = self._text[self._idx]
        except:
            raise StopIteration("Stop Iteration. ^________^")
        self._idx += 1
        return word
    
    def __repr__(self):
        return "WordSplitIterator(%s)" % (self._text)
    
wi = WordSplitIterator("Do today what you could do tomorrow")
print(wi)

print(next(wi)) # 클래스 객체인데 Iterable하게 사용하고있음
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi)) # 예외 발생

print()
print()


# 2. Generator Pattern
class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(" ") # 인덱스값 필요없음
        
    def __iter__(self): # 예외처리 해줄 필요도 없음
        for word in self._text:
            yield word # return 대신 yield 사용
        return
    
    def __repr__(self):
        return "WordSplitGenerator(%s)" % (self._text)

wg = WordSplitGenerator("Do today what you could do tomorrow")
wt = iter(wg)

print("wg: ", wg)
print("wt: ", wt)

print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))