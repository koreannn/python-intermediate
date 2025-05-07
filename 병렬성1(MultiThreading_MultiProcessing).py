"""
- future 패키지
- 코루틴: 하나의 흐름에서 다양한 작업을 수행하는 것
- 동시성: 여러 작업을 동시에 수행하는 것
    - Futures(동시성)
        - 비동기 작업 처리
        - 파이썬 GIL(Global Interface Lock)
        - 동시성 처리 실습 
        - Process & Thread 실습
- 지연 시간(Block) CPU 및 리소스 낭비 방지 (e.g. (File)Network I/O관련 작업에서 동시성 활용 권장)
- 비동기 작업과 적합한 프로그램일수록 성능이 훨씬 향상됨
"""


"""Futures 동시성 - 비동기 작업 실행"""
import os
import time
from concurrent import futures # 패키지 내부 -> threading, multiprocessing..

WORK_LIST = [100000, 1000000, 10000000, 100000000]
# WORK_LIST = [내가 원하는 작업 1, 내가 원하는 작업 2, 내가 원하는 작업 3, 내가 원하는 작업 4 ...]

def sum_generator(n):
    return sum(n for n in range(1, n+1)) # 1~10000까지의 합, 1~100000까지의 합, 1~1000000까지의 합, 1~10000000까지의 합

def main():
    worker = min(10, len(WORK_LIST)) # 4

    start_time = time.time() # 시작 시간
    result = []
    # # 1. ProcessPoolExecutor - (현재 프로세스 내에서 만들어진)쓰레드로 실행
    # with futures.ThreadPoolExecutor() as executor:
    #     result = executor.map(sum_generator, WORK_LIST)
        
    # 2. ThreadPoolExecutor - 프로세서로 실행(CPU로 실행)
    with futures.ProcessPoolExecutor() as executor:
        result = executor.map(sum_generator, WORK_LIST) # (쓰레드보다는 조금이나마 더 빠름)
    
    end_time = time.time() # 종료 시간
    msg = "\nResult -> {} Time: {:.2f}s"
    
    print(msg.format(list(result), end_time - start_time))

if __name__ == "__main__":
    main()

