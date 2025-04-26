"""
시퀀스형
파이썬 자료구조:
    1. 컨테이너 형태: 서로다른 타입을 저장할 수 있는 자료구조(list, tuple, collections.deque ..)
    2. 플랫(Flat)형태: 한 가지 타입만 저장할 수 있는 자료구조(str, bytes, bytearray, array.array, memoryview ..)
가변형: list, bytearray, array.array, memoryview, collections.deque
불변형: tuple, str, bytes

리스트 및 튜플 고급
"""

"""지능형 리스트(Comprehending list)"""
strings = "+_)(*&^%$#@!)"
# strings[2] = '~' # 불가능
code_list1 = []
for s in strings:
# 유니코드 리스트
	code_list1.append(ord(s))
print(code_list1)


# 지능형 리스트(Comprehending list)
code_list2 = [ord(s) for s in strings]
print(code_list2)


# 번외1. Comprehending list + Map + Filtering
code_list3 = [ord(s) for s in strings if ord(s) > 40] # if문으로 필터링
code_list4 = list(filter(lambda x: x>40, map(ord, strings))) # filter, map으로 조건 걸어주기
print(code_list3)
print(code_list4)


# 번외2. 다시 원래대로 변환
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])

print()
print()


"""Generator"""
# 파이썬에는 배열이 없는게 아니라, array 모듈이 분명히 존재한다.
import array

# 제너레이터: 한 번에 한 개의 항목을 생성(메모리 유지 x)
tuple_g = (ord(s) for s in strings)
print(tuple_g)
print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(dir(tuple_g))

array_g = array.array("I", (ord(s) for s in strings))
print(array_g)
print(type(array_g))
print(array_g.tolist())

print()
print()


# 사용 예시 (각 학급마다 20명의 학생 만들기)
example_generator = ("Class %s"%c + " Number"+str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21))
print(example_generator)

for student in example_generator:
    print(student)

print()
print()


"""리스트에서 주의할 점 - 파이썬의 깊은 복사와 얕은 복사"""
marks1 = [["~"]*3 for _ in range(4)] # [["~", "~", "~"], ["~", "~", "~"], ... ["~", "~", "~"]] / 깊은 복사
marks2 = [["~"]*3]*4 # [["~", "~", "~"], ["~", "~", "~"], ... ["~", "~", "~"]] / 얕은 복사

marks1[0][1] = "O"
marks2[0][1] = "O"

print(marks1)
print(marks2) 

print([id(i) for i in marks1])
print([id(i) for i in marks2])