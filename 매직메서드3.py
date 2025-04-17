# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

from collections import namedtuple
from math import sqrt

"""1. 그냥 무지성 튜플 사용할 경우"""
pt1 = (3.0, 4.0)
pt2 = (5.0, 10.0)
print("pt1: ", pt1)
print("pt2: ", pt2)

l_leng1 = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
print("l_leng1: ", l_leng1)
print()

"""2. NamedTuple 활용"""
# NamedTuple 선언하기
Point = namedtuple("Point", "x y")

pt3 = Point(3.0, 4.0)
pt4 = Point(5.0, 10.0)
print(f"type of {type(pt3)}, {type(pt4)}")
print("pt3: ", pt3)
print("pt4: ", pt4)

l_leng2 = sqrt((pt3[0]-pt4[0])**2 + (pt3[1]-pt4[1])**2)
# 더 좋은 표현은 아래(key값으로 접근하기)와 같음
l_leng3 = sqrt((pt3.x-pt4.x)**2 + (pt3.y-pt4.y)**2)
print("l_leng2: ", l_leng2)
print("l_leng3: ", l_leng3)
print()

"""3. NamedTuple을 선언하는 여러 가지 방법"""
Point1 = namedtuple("Point", ['x', 'y'])
Point2 = namedtuple("Point", "x, y")
Point3 = namedtuple("Point", "x y")

Point4 = namedtuple("Point", "x y x class", rename=True)

print("Point1, Point2, Point3, Point4: ", Point1, Point2, Point3, Point4)

# dict 2 Unpacking
# 전달하는 딕셔너리의 키 이름은 사용할 namedtuple의 필드 이름과 정확히 일치해야한다.
# 즉 "x", "y" 말고 key이름을 다른거로 하면 안됨
tmp_dict = {"x": 75, "y": 55}

# 객체 생성
p1 = Point1(10, 35)
p1 = Point1(x=10, y=35)
# 둘 다 상관없다. 명시적으로 쓰고싶으면 두 번째처럼 쓰면 된다.

p2 = Point2(20, 40)
p3 = Point3(45, y=20)
# rename옵션 써보기
p4 = Point4(10, 20, 30, 40)
# 딕셔너리에 대해 Unpacking해보기
p5 = Point3(**tmp_dict) # Point1, 2, 3 중에 뭘 쓰든 상관없다.

print()
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)


"""4. 사용해보기"""
print(p1[0] + p2[1]) # 안되는건 아니지만 이렇게 쓰진 말자
print(p1.x + p2.y)

# Unpacking
p2_x_point, p2_y_point = p2
print(p2_x_point, p2_y_point)


"""5. NamedTuple 메서드"""
# 해당 네임드 튜플 객체에 어떤 key값이 있는지 조회
print("p1._fields, p2._fields, p3._fields, p4._fields: ", p1._fields, p2._fields, p3._fields, p4._fields)

# 새로운 객체 생성(다만 인자의 개수는 맞춰서 넣어줘야함)
tmp_list = [30, 40]
p6 = Point1._make(tmp_list)
print("p6: ", p6)

# '정렬된 딕셔너리(OrderedDict)'를 반환 (NamedTuple -> dictionary 변환)
print("p1._asdict(): ", p1._asdict())
print("p4._asdict(): ", p4._asdict())


"""6. 사용할법한 실제 예시"""
# 4개의 반(A, B, C, D)에 대해 각 20명씩 존재
Classes = namedtuple("Classes", ["rank", "number"])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)] # 1번~20번
ranks = "A B C D".split() # A, B, C, D반의 성적순위라고 하자.

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students)

# 더 추천하는 방식
students2 = [Classes(rank, number)
			for rank in "A B C D".split()
				for number in [str(n) for n in range(1, 21)]]

print(len(students2))
print(students2)

print()
for s in students:
	print(s)