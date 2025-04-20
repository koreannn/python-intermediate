# HashTable = Key-Value Pair로 이루어진 데이터구조
# 파이썬은 해시테이블을 직접 구현할 필요 없음 (딕셔너리가 곧 해시테이블)
# Key값의 연산 결과에 따라 "직접" 접근이 가능한 구조이다.
# 전체 흐름: Key값 -> Hash Function -> Hash Value -> Key -> Key에 대한 Value 참조

"""HashTable 예제 - 해시값을 통해 데이터를 참조할 수 있는 경우와 없는 경우"""
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print("Hash value of t1: ", hash(t1)) # 해당 해시값을 통해 이 튜플을 참조할 수 있음
# print(hash(t2)) # 리스트가 포함됨 (해시값으로 다룰 수 없는 데이터 구조)

print()
print()


"""Dict Setdefault 예제"""
source = (('k1', 'val1'), 
            ('k1', 'val2'), 
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}
# Key-Value형태로 이루어지지 않은 데이터에 대해, Key-Value형태로 변경해야 할 경우
# 1. Setdefault를 사용하지 않고 변경할 경우
for k, v in source:
    if k not in new_dict1:
        new_dict1[k] = [v] # Value는 리스트로 저장
    else:
        new_dict1[k].append(v)
print("new_dict1: ", new_dict1)

# 2. Setdefault를 사용하여 변경할 경우
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
print("new_dict2: ", new_dict2)


# 주의사항
new_dict3 = {k: v for k, v in source}
print("new_dict3: ", new_dict3)

new_dict4 = dict(source)
print("new_dict4: ", new_dict4)

