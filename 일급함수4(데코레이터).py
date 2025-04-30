"""
- 클로저 -> 데코레이터
- 데코레이터 실습
"""

# '함수 위에 @로 달아주는것'

# 중복 제거, 코드 간결, 공통함수 작성
# 로깅, 프레임워크, 유효성 체크 -> 공통 함수(공통 기능) 작성 가능
# 조합해서 사용하기 편함 .. 등

# 너무 많이쓰면 가독성이 떨어질수도 있음
# 특정 기능에 한정한 함수는 단일 함수로 작성하는것이 유리함.
# 디버깅이 약간 불편함

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

# 각 함수를 perf_clock에 넘겨주면, 해당 함수들이 perf_clock 내에서 실행되는거임 (그 함수의 상태를 갖게된다고도 볼 수 있으므로, 일종의 클로저라고 볼 수 있음)
# 어쨌든 perf_clock과 같은 함수 한 번만 만들어두면, 그 이후에 함수를 몇 개를 만들던 각 함수들에 대한 시간 정보(로깅)를 출력할 수 있음. 이게 데코레이터.



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


# 데코레이터를 붙여주면, 해당 함수가 호출되기 전에 데코레이터에 정의된 함수가 먼저 실행됨 (데코레이터에 정의해둔 동작을 추가적으로 작성하지 않아도 원하는 동작을 공통적으로 얻을 수 있음)
# 데코레이터를 붙여주면 그 함수 자체를 호출해도 원하는 동작을 얻을 수 있음
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