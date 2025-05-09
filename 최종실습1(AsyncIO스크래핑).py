"""
AsyncIO: 코루틴에서 좀 더 확장된 비동기 IO 라이브러리
Generator: 반복적인 객체 Return 사용 -> Nonblocking(비동기)
AsyncIO: 동시성 처리를 가능하게 하는 라이브러리(async, await) -> 큐를 기반으로 동작한다... 등 (구체적인 내용은 스스로 찾아보기)
Blocking IO: 호출된 함수가 자신의 작업이 완료될때까지 제어권을 가지고있음(다른 함수는 이 함수가 끝날때까지 대기)
Non-Blocking IO: 호출된 함수(서브루틴)가 return 후 호출한 함수(메인루틴)에 제어권을 전달함으로써, 다른 함수는 일을 지속할 수 있음

AsyncIO를 쓴다고 하더라도, 내가 쓰고자하는 함수가 Blocking 함수일 경우, AsyncIO를 쓰는 의미가 없다. (오히려 단일 쓰레드로 만드는게 빠르다.)
즉 내가 사용할 함수도 비동기로 구현되어있어야한다(Generator처럼)

쓰레드 단점: 디버깅, 자원 접근 시 경쟁상태(Race Condition)발생, 데드락(Dead Lock).. 과 같은 것들을 고려하며 코딩해야함
코루틴 장점: 하나의 루틴만 실행, 락을 관리할필요 없음, 제어권을 가지고 실행.. (단점은, 사용하는 함수가 비동기로 구현되어있어야한다는 점)

- async, await 설명 및 프로그램 테스트
"""

# urlopen은 Block IO함수 -> 따라서 쓰레드를 통해 urlopen을 따로(비동기로)실행한다면 asyncio를 쓰는 의미를 만들 수 있음

import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 시작시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장
urls = ['https://www.daum.net', 'https://www.naver.com', 'https://www.google.com', 'https://www.tistory.com']

async def fetch(url, executor):
    # 쓰레드 명 출력
    print(f"Thread Name: {threading.current_thread().getName()} Start URL: {url}")
    # 실행
    response = await loop.run_in_executor(executor, urlopen, url)
    print(f"Thread Name: {threading.current_thread().getName()}, Done URL: {url}") # 종료되는 순서가 다름 -> 비동기로 실행되기때문에
    
    # 결과 반환
    return response.read()


async def main():
    # ThreadPool 생성
    executor = ThreadPoolExecutor(max_workers=10) # Thread를 사용한 이유: urlopen이 Blocking 함수이기 때문에 (Thread를 사용하지 않으면, 의도와 달리 순차적으로 실행됨)
    
    # Future 객체를 모아서 gather에서 실행
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    result = await asyncio.gather(*futures) # Unpacking -> 비동기로 실행되는 함수들의 결과를 "모아서" 반환
    
    print()
    print()
    # print(result)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # 작업 완료까지 대기
    loop.run_until_complete(main())
    # 수행시간 계산
    duration = timeit.default_timer() - start
    print(f"수행시간: {duration}초")
