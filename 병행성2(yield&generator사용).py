"""Generator Example 1"""
def generator_ex1():
    print('Start')
    yield 'A Point'
    print('Continue')
    yield 'B Point'
    print('End')

tmp = iter(generator_ex1())

print("tmp: ", tmp)
print("next(tmp) 1: ", next(tmp))
print("next(tmp) 2: ", next(tmp))

for v in generator_ex1():
    print(v)


print()
print()


# Generator Example2
tmp2 = [x * 3 for x in generator_ex1()]
tmp3 = (x * 3 for x in generator_ex1())

print("tmp2: ", tmp2)
print("tmp3: ", tmp3)


for v in tmp2:
    print(v)

print()
for v in tmp3:
    print(v)

print()
print()

"""Generator에서 중요시되는 함수 몇 가지"""
# filterfalse, accumulate, chain, product, groupby... -> 데이터를 센스있게 만들어낼 수 있음

# 1. itertools활용
import itertools

gen1 = itertools.count(1, 2.5)
print("gen1: ", gen1)
print("Value of gen1 by next(): ", next(gen1), next(gen1), next(gen1), end=' ')
# ... Infinite
print()

# 조건을 걸고싶을경우
gen2 = itertools.takewhile(lambda n: n<1000, itertools.count(1, 2.5))
for v in gen2:
    print(v, end=' ')

print()

# filterfalse
gen3 = itertools.filterfalse(lambda n: n<3, [1,2,3,4,5]) # 3보다 작은 값은 필터링함 (4,5만 남음)
for v in gen3:
    print(v, end=' ')

print()

gen4 = itertools.accumulate([x for x in range(1, 10)]) # 누적합
for v in gen4:
    print("Value of gen4: ", v) # 1, 1+2, 1+2+3, ...

print()

# 연결 (Chaining)
# 서로 다른 Iterable을 연결해서 하나로 합치고싶을 때
gen5 = itertools.chain("ABCDE", range(1, 11, 2))
print("gen5: ", gen5)
print("next(gen5): ", next(gen5)) 
print("Value of gen5: ", list(gen5))
for v in iter(gen5): # 제너레이터는 메모리 효율성을 위해 한 번만 순회할 수 있도록 설계됨
    print(v, end=' ')

print()

# Chaining2
gen6 = itertools.chain(enumerate("ABCDE"))
print("gen6: ", gen6)
print("list(gen6): ", list(gen6))
print()

print()

# product
gen7 = itertools.product("ABCDE")
print("gen7: ", gen7)
print("list(gen7): ", list(gen7))
print()
gen8 = itertools.product("ABCDE", repeat=2) # 중복 허용해서 두 개를 뽑는 모든 경우의 수 (5*5 = 25)
print("len(list(gen8)): ", len(list(gen8)))
print("gen8: ", gen8)
print("list(gen8): ", list(gen8))
print()

# groupby
gen9 = itertools.groupby("AABBCCCDEEE")
print("gen9: ", gen9)
# print("list(gen9): ", list(gen9))
for k, v in gen9:
    print(k, " : ", list(v))