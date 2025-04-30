"""
클로저 심화
- 클로저 사용 예시
- 잘못된 클로저 사용 예시
- 클로저 최종 정리
"""

"""Closure 사용 예시"""
class Averager(): # 평균을 구해서 누적하는 클래스
    def __init__(self):
        self._seriese = []
        
    def __call__(self, v): # 클래스를 함수처럼 호출할 수 있게 하는 매직메서드
        self._seriese.append(v)
        print("inner: {} / {}".format(self._seriese, len(self._seriese)))
        return sum(self._seriese)/len(self._seriese)

# 위 클래스를 Closure로 똑같이 구현할 것이다.
def closure_ex1():
    series = [] # Free Variable(자유 변수)
    def averager(v):
        series.append(v)
        print("inner: {} / {}".format(series, len(series)))
        return sum(series)/len(series)
    return averager # 함수를 리턴!! 
    #return averager() # 함수 자체를 리턴해야지, 함수 호출 결과를 리턴하면 안된다.

avg_closure1 = closure_ex1()
print(avg_closure1(10))
print(avg_closure1(30))
print(avg_closure1(50))
print()
print()


"""Function Inspection"""
print(dir(avg_closure1))
print()
print(avg_closure1.__code__) 
print(dir(avg_closure1.__code__)) 
print(avg_closure1.__code__.co_freevars) # 자유 변수들을 튜플로 저장하고있음
print(avg_closure1.__closure__) 
print(avg_closure1.__closure__[0])
print(avg_closure1.__closure__[0].cell_contents) # 자유 변수들의 실제 값을 확인할 수 있음
print()
print()


"""Closure의 잘못된 사용 예시"""
def closure_ex2():
    # Free Variable
    cnt = 0
    total = 0
    def averager(v):
        cnt += 1 
        total += v
        return total/cnt
        # return
    return averager

avg_closure2 = closure_ex2()
print(avg_closure2(10)) # 예외가 발생

# 올바른 예
def closure_ex3():
    # Free Variable
    cnt = 0
    total = 0
    def averager(v):
        nonlocal cnt, total # cnt와 total을 Free Variable로 인식하도록
        cnt += 1
        total += v
        return total/cnt
    return averager

avg_closure3 = closure_ex3()
print(avg_closure3(10))
print(avg_closure3(30))
print(avg_closure3(50))
print()
print()
