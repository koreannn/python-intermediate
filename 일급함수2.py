"""
- 클로저 기초
    - 파이썬의 변수 범위(Scope) / Global 선언
    - 클로저를 사용하는 이유
    - Class 형태로 Closure 구현해보기
    클로저 = 내 범위 내에 있는 변수의 상태를 저장하는 스냅샷
    다음시간에는 클로저를 기반으로 데코레이터가 파생됨
    클로저는 동시성/병행성의 중간다리 역할임
"""


"""변수의 범위"""
# # Ex1.
# def func1(a):
#     print(a)
#     print(b)

# func1(10)

# Ex2.
b=20
def func2(a):
    print(a)
    print(b)
func2(10)
print()
print()

# # Ex3.
# c=30
# def func3(a):
#     print(a)
#     print(c)
#     c=30
# func3(10)
# Ex3-1.
c=30
def func3(a):
    c=40
    print(a)
    print(c)

func3(10) # Local이 우선적으로 참조됨
print()
print()

# Ex3-2.
c=30
def func4(a):
    global c # 함수 내에서 global 키워드 쓰는거 좋은 코딩은 아님
    print(a)
    print(c)
    c=40

func4(10)


"""Closure"""
# Ex1.
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c = make_counter()
print(c(), c(), c())  # 1 2 3 — count 상태가 유지됨
print()
print()

# Ex2. (클래스로 클로저의 동작 방식을 비슷하게 구현)
class Averager(): # 평균을 구해서 누적하는 클래스
    def __init__(self):
        self._seriese = []
        
    def __call__(self, v): # 클래스를 함수처럼 호출할 수 있게 하는 매직메서드
        self._seriese.append(v)
        print("inner: {} / {}".format(self._seriese, len(self._seriese)))
        return sum(self._seriese)/len(self._seriese)

averager_cls = Averager()
print(averager_cls(10)) # 클래스를 함수처럼 쓰고있음
print(averager_cls(30))
print(averager_cls(50)) # 자유 영역에 있는 상태를 기억하고있음(계속 유지됨)