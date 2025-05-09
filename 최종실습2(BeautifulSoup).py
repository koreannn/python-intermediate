import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import threading

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8') # 한글 깨짐 방지용

start = timeit.default_timer()

urls = ['https://www.daum.net', 'https://www.naver.com', 'https://www.google.com', 'https://www.tistory.com']

async def fetch(url, executor):
    print(f"Thread Name: {threading.current_thread().getName()} Start URL: {url}")
    # 실행
    response = await loop.run_in_executor(executor, urlopen, url)
    
    soup = BeautifulSoup(response.read(), 'html.parser')
    
    # 전체 페이지 소스 확인
    # print(soup.prettify())
    
    # 원하는 데이터 추출
    result_data = soup.title
    print(f"Title: {result_data}")
    
    
    # print(f"Thread Name: {threading.current_thread().getName()}, Done URL: {url}") 
    
    # 결과 반환
    return response.read()


async def main():
    executor = ThreadPoolExecutor(max_workers=10) 
    
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    result = await asyncio.gather(*futures) 
    
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
