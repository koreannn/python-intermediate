"""
- 해시테이블: 적은 리소스로 많은 데이터를 효율적으로 관리
- Dict -> key 중복 허용X, Set
- 원래 딕셔너리와 Set은 Mutable하지만, Immutable하게 선언할수도 있음
"""
from types import MappingProxyType

"""Dictionary"""
d = {"key1": "val1"} 
d_frozen = MappingProxyType(d) # 읽기 전용(Immutable)의 딕셔너리
print("d: \n", d, "id of d: ", id(d))
print("d_frozen: \n", d_frozen, "id of d_frozen: ", id(d_frozen))

# Test
d["key2"] = "val2" 
# d_frozen["key2"] = "val2" # 변경 불가능
print("d: \n", d, "id of d: ", id(d))
print("d_frozen: \n", d_frozen, "id of d_frozen: ", id(d_frozen)) # 원본(d)을 변경하면, 읽기 전용의 딕셔너리(d_frozen)도 변경됨
# 둘 다 해시값을 반환할수는 없음

print()
print()

"""Set"""
s1 = {"apple", "banana", "cherry"}
s2 = set(["apple", "banana", "cherry"])
s3 = {3}
s4 = {}
s5 = frozenset(["apple", "banana", "cherry"])

print("type(s1): ", type(s1))
print("type(s2): ", type(s2))
print("type(s3): ", type(s3))
print("type(s4): ", type(s4))
print("type(s5): ", type(s5))

print("s1: ", s1)
s1.add("melon")
print("s1: ", s1)
# s5.add("Melon") # 불가능

print()
print()

# 선언 최적화 Tip
# 파이썬은 바이트 코드를 실행 (바이트 코드 -> 파이썬 인터프리터)
from dis import dis
print(dis('{10}')) # 이게 미세하지만 더 빠르다.
print(dis('set([10])'))

print()
print()

# 지능형 Set (Comprehending Set) 만들기 예시

from unicodedata import name
print(chr(i) for i in range(0, 256))
print({name(chr(i), "") for i in range(0, 256)})

