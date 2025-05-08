"""
- Futures wait 예제
- Futures as_completed
- 동시 실행 결과 출력
- 동시성 처리 응용 예제 

동시성 처리는 내부적으로 두 가지가 존재: wait, as_completed
사용법1: map
사용법2: wait, as_completed
    wait: 지정한 시간까지 기다리는 것
    as_completed: 먼저 끝난 작업부터 반환하는 것
"""
import os
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait, as_completed

WORK_LIST = [1000000, 10000000, 100000000, 1000000000]

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    worker = min(10, len(WORK_LIST))

    start_time = time.time() 
    futures_list = []

    with ProcessPoolExecutor() as executor: # 또는 ThreadPoolExecutor
        for work in WORK_LIST:
            future = executor.submit(sum_generator, work) # futures만 반환할 뿐, 실행하는건 아님(미래에 할 일을 일단 반환한 것)
            futures_list.append(future) # 할 일을 futures_list에 넣어줌 
            print("Scheduled for {}: {}".format(work, future)) # 작업에 대한 스케쥴링 확인
            print()
        
        """1. wait"""
        result = wait(futures_list, timeout=7) # 7초를 임계점으로 두고, 7초를 초과하는 작업에 대해서는 실패로 간주
        # 성공한 작업
        print("Completed tasks: {}".format(str(result.done))) # 7초를 초과한 작업은 추가되지않음
        print()
        # 실패한 작업
        print("Pending ones after waiting for 7 seconds: {}".format(str(result.not_done)))
        print()
        # 결과값 출력
        print([future.result() for future in result.done])
        print()
        
        print("--------------------------------")
        
        """2. as_completed"""
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled()
            print("Future result: {}\nDone: {}\nCancelled: {}".format(result, done, cancelled))
            print()
        
        
    end_time = time.time()
    msg = "\nResult -> {} Time: {:.2f}s"
    
    print(msg.format(list(futures_list), end_time - start_time))

if __name__ == "__main__":
    main()
    