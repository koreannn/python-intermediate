"""
- 오픈소스 등 다른사람 코드 보면 무슨 표현인지 이해가 안가는경우가 꽤 많다. 파이썬의 여러 표현 방식때문이다.
좀 두서없더라도, 이에 대해 대충이라도 정리해보자.
"""

"""파이썬의 tmp"""
a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

print()
print()


"""Tuple advanced"""
# Unpacking
print(divmod(100, 9)) # 몫과 나머지를 반환하는 함수
print(divmod(*(100, 9))) # 명시적으로 튜플을 넣어주는 표현을 사용하고싶다면 이와 같이 언패킹을 명확하게 해줘야한다.
print(*divmod(100, 9)) # 몫과 나머지를 반환하는 함수를 언패킹하여 출력

# x, y, rest = range(10) # 에러 발생
x, y, *rest = range(10) # 언패킹을 사용하여 몫과 나머지를 반환하는 함수를 언패킹하여 출력
x2, y2, *rest2 = range(2)
x3, y3, *rest3 = range(3)
print(x, y, rest)
print(x2, y2, rest2)
print(x3, y3, rest3)

print()
print()


"""Mutable(가변형) vs Immutable(불변형)"""
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2 # __mul__
m = m * 2 # __mul__

print(l, id(l))
print(m, id(m))

l *= 2 # __imul__이 없으므로, __mul__이 대신 호출됨
m *= 2 # __imul__이 있으므로, __imul__이 수행됨(__mul__과 달리 원본을 직접 수정)

print(l, id(l))
print(m, id(m))

print()
print()


"""파이썬의 정렬 (sort, sorted = inplace, not inplace)"""
# reverse옵션 / key = len, key = str.lower, key = func ... (사용자 정의 함수, 람다함수 등)
# sort: in-place정렬 (원본을 직접 수정 (새로운 할당 x))
# sorted: not in-place정렬 (수정된 결과를 새로운 객체에 반환)
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print("Original: ", f_list)

# 1. sorted()
print("Sorted: ", sorted(f_list))
print("Sorted(reverse=True): ", sorted(f_list, reverse=True))
print("Sorted(key=len): ", sorted(f_list, key=len))
print("Sorted(key=lambda x: x[-1]): ", sorted(f_list, key=lambda x: x[-1]))

print()
print()
# 2. .sort()
print("Original: ", f_list)
print("Sort: ", f_list.sort(), f_list) # f_list.sort()의 반환값은 None
print("Sort(reverse=True): ", f_list.sort(reverse=True), f_list)
print("Sort(key=len): ", f_list.sort(key=len), f_list)
print("Sort(key=lambda x: x[-1]): ", f_list.sort(key=lambda x: x[-1]), f_list)

print()
print()


"""List vs Array의 각각 적합한 사용법 설명"""
# List: 융통성, 범용적인 사용 (e.g. 다양한 자료형 지원 등)
# Array: 수치 연산 및 벡터 연산 등 효율적인 사용 (e.g. 수치 연산 및 벡터 연산 등)
# Array는 리스트와 호환성이 매우 높음(매서드 등이 거의 동일함)

