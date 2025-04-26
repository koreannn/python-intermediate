"""
파이썬 일급 함수(일급 객체)
    파이썬 함수 특징
    익명함수(lambda)
    Callable 객체
    Partial 설명
"""


"""함수는 객체 취급된다."""
def factorial(n):
    """
    Factorial Function
    args: n (int)
    return: n!
    """
    if n == 1:
        return 1
    return n * factorial(n-1)

class A:
    pass

print(factorial.__doc__)
print("type of factorial(): ", type(factorial)) # 객체로 취급됨
print("type of Class A: ", type(A))

# 객체취급된다는 것은 아래 출력을 통해 확실하게 알 수 있다.
print("dir(factorial): ", dir(factorial))
print()
print("set(sorted(dir(factorial))) - set(sorted(dir(A))): ", set(sorted(dir(factorial)))-set(sorted(dir(A))))# 함수만이 갖는 Attribute
print("factorial.__name__: ", factorial.__name__)
print("factorial.__code__: ", factorial.__code__) # 함수가 어디에 존재하는지 확인할 수 있음
print("factorial.__closure__: ", factorial.__closure__)
print("factorial.__defaults__: ", factorial.__defaults__)
print("factorial.__kwdefaults__: ", factorial.__kwdefaults__)

print()
print()

# 함수를 변수에 할당
var_func = factorial

print(var_func)
print(var_func(10))
print(list(map(var_func, range(1, 11))))

print()
print()


"""함수를 함수의 인자로 전달 및 함수를 리턴값으로 반환 -> 고위 함수(Higher-Order Function)"""
# map, filter
print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i % 2])
# 코드의 가독성은 2번이 더 좋지만 중요한것은, 1번 예시의 경우에서 함수 자체를 인수로 전달했다는것(람다함수)

# reduce
from functools import reduce
from operator import add # +랑 똑같은건데, 더 엄격하게 작성하기 위해
print(sum(range(1,11)))
print(reduce(add, range(1,11))) # 각 요소 하나하나를 죽여가면서(reduce) 누적으로 더해가는 방식
# sum(range...)가 더 빠르긴 함

# 익명함수(lambda)
# 익명함수보단 그냥 함수를 쓰고, 꼭 써야한다면 주석을 달아주자.
print(reduce(lambda x, t: x+t, range(1,11)))

print()
print()


"""callable, partial"""
# callable: 호출 연산자(메서드 형태로 호출 가능한지 확인할때 사용)
print(callable(str)) # str("a") 이런식으로 호출이 가능하므로, True
print(callable(A))
print(callable(var_func))
print(callable(list))
print(callable(factorial))
print(callable(3))

# (참고)inspect 모듈
from inspect import signature

sg = signature(var_func)

print("sg: ", sg)
print("sg.parameters: ", sg.parameters)

print()
print()

# partial 사용법: 인수 고정 시 사용(콜백 함수에서 주로 사용)
from operator import mul
from functools import partial

print(mul(10, 10))

# 인수 고정
five = partial(mul, 5) # mul 함수 중 인수 5는 고정 (5 * x 형태로 만들어줌)
print(five(10)) # x값에 10을 넣어줌

# 고정 추가
six = partial(five, 6) # 5*6이됨
print(six())
# print(six(10)) 에러 발생
print([five(i) for i in range(1, 10)]) # 구구단의 5단
print(list(map(five, range(1, 10))))