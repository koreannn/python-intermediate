"""
- 클로저 -> 데코레이터
- 데코레이터 실습
"""


"""데코레이터 실습(사용했을 때와 하지 않았을 떄의 비교)"""
import time
from typing import Callable, Any

def perf_clock(func: Callable) -> Callable:
    
    def perf_clocked(*args) -> Any:
        start_time = time.perf_counter() # 함수 시작 시간
        result = func(*args) # 함수 실행
        end_time = time.perf_counter() # 함수 종료 시간
        name = func.__name__ # 함수 이름
        arg_str = ", ".join(repr(arg) for arg in args) # 함수의 매개변수들 (generator)
        
        print("[%0.5fs] %s(%s) -> %r" % (end_time - start_time, name, arg_str, result)) # 결과 출력
        return result
    return perf_clocked

def time_func(seconds):
    time.sleep(seconds)
    return
    
def sum_func(*numbers):
    return sum(numbers)

# 데코레이터를 사용하지 않았을 때
none_deco1 = perf_clock(time_func)
none_deco2 = perf_clock(sum_func)

print("none_deco1:", none_deco1)
print("none_deco1.__code__:", none_deco1.__code__.co_freevars)
print("none_deco2:", none_deco2)
print("none_deco2.__code__:", none_deco2.__code__.co_freevars)
print()
print()

print("-"*40, "Called None Decorator -> time_func")
none_deco1(1.5) 
print()
print("-"*40, "Called None Decorator -> sum_func")
none_deco2(100, 200, 300, 400, 500)
# 이와 같이 데코레이터를 사용하지 않으면, 내부 함수를 다시 끄집어내서 사용해야한다는 단점이 있음

print()
print()


# 데코레이터를 사용할 때
@perf_clock
def time_func_with_deco(seconds):
    time.sleep(seconds)
    return

@perf_clock
def sum_func_with_deco(*numbers):
    return sum(numbers)

print("-"*40, "Called Decorator -> time_func")
time_func_with_deco(1.5) 
print()

print("-"*40, "Called Decorator -> sum_func")
sum_func_with_deco(100, 200, 300, 400, 500)