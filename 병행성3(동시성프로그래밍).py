"""
- yield & send -> main ~ sub의 상호작용
- 쓰레드: OS에서 관리, CPU 코어 실시간, 시분할 비동기 작업 (by 멀티쓰레드)
- 코루틴: "단일한" 쓰레드에서 스택을 기반으로 동작하는 비동기작업 (리소스가 부족한 환경에서도 병렬처리가 가능한~)
    - 코루틴은 파이썬뿐만 아니라 모든 언어에서 사용 가능
    -  코루틴 제어 시 yield 키워드가 핵심
- 코루틴 제어, 상태, 양방향 전송

- 서브 루틴: 메인 루틴에서 호출되어 실행되는 루틴(수동적)
- 코루틴: 루틴 실행 중 중지 후 다른작업 수행 가능 (시점을 "기억"하고있으므로) -> "동시성 프로그래밍"
- 쓰레드에 비해 오버헤드를 감소시킬 수 있음(OS에 많은 쓰레드를 요청하지 않아도 되므로)
- 쓰레드: 싱글 쓰레드 ~ 멀티쓰레드 
    - 멀티 쓰레드: 복잡, 공유되는 자원, 교착상태 발생 가능성, context switching 비용 발생, 자원 소비 가능성 증가
    - 멀티 쓰레드보다 오히려 싱글 쓰레드가 더 빠른 경우가 종종 있는데, 이는 스위칭 비용으로 인한 성능 저하때문
"""

def coroutine1(): # def이라고 모두 함수인건 아니다. 제너레이터나 코루틴도 def으로 시작된다.
    print(">>> Coroutine started")
    i = yield
    print(">>> Coroutine received: {}".format(i))

# 메인 루틴 (코루틴 내부가 서브 루틴)
cr1 = coroutine1()

print("cr1: ", cr1, "\n", "type(cr1): ", type(cr1))
# print(next(cr1))
next(cr1) # yield 지점까지 서브루틴을 수행
# next(cr1) 


# 기본 전달값(send()에 인자값을 넣지 않을 경우)은 None
# cr1.send(100)

print()
print()

"""잘못된 사용"""
# 코루틴을 시작하지도 않고 바로 값을 전달할수는 없음
cr2 = coroutine1()
# cr2.send(100) # 예외 발생



"""코루틴 예시2"""
# GEN_CREATED
# GEN_RUNNING
# GEN_SUSPENDED
# GEN_CLOSED

def coroutine2(x):
    print(">>> coroutine started:{}".format(x))
    y = yield x
    print(">>> coroutine received:{}".format(y))
    z = yield x + y # 핵심은 인자값(메인루틴에서 전달받은 값)과 서로 데이터를 주고받는다는 것
    print(">>> coroutine received:{}".format(z))
    
cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))
print(next(cr3))

print(getgeneratorstate(cr3))
print(cr3.send(100))

print(getgeneratorstate(cr3))
cr3.send(100)


"""코루틴 예시3"""
# 파이썬 3.5이상부터는 def를 async, yield를 await으로 사용가능
# await은 StopIteration도 자동으로 처리해줌
# 중첩 코루틴 처리

def generator1():
    for x in "AB":
        yield x
    
    for y in range(1, 4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()
print(list(t2))


def generator2():
    yield from "AB"
    yield from range(1, 4)

t3 = generator2()

print(next(t3))
print(next(t3))
