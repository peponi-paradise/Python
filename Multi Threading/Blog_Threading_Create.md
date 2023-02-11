<h1 id="Title">Thread를 생성하는 방법</h1>

- Thread를 생성하는 방법은 여러가지가 있다. 여기서는 `Thread`, `ThreadPool`, `Concurrent.futures`를 이용하는 방법을 소개한다.
<br><br>

<h2 id="Thread">Thread</h2>

```
from threading import Thread
from time import sleep

def ProcessThreadFunction():
    print("Thread created")
    print("Work start")
    print("Working...")
    sleep(1)
    print("Work done")

if __name__=="__main__":

    worker=Thread(target=ProcessThreadFunction)
    worker.daemon=True
    worker.start()
    worker.join()
    print("Thread work has been done")
```
<br>

- Thread 생성자를 이용하여 호출한다.[footnote][Python Threading - 생성 및 기본 사용법](https://peponi-paradise.tistory.com/entry/Python-Threading-Basic)[/footnote]
<br><br>

<h2 id="ThreadPool">ThreadPool</h2>

```
from multiprocessing.pool import ThreadPool

def ThreadFunction(ThreadIndex:int):
    print("Thread start")

    print(f"Thread number : {ThreadIndex}")

    return ThreadIndex

if __name__=="__main__":

    ThreadCount=10
    ThreadExec=ThreadPool(ThreadCount)
    for Result in ThreadExec.map(ThreadFunction,range(ThreadCount)):
        print(f"{Result} Thread Done")

    print(f"Thread work has been done")
```
<br>

- Multiprocessing의 threadpool을 이용한다. 분할된 작업을 병렬로 실행하기 좋고, 결과를 받아오기 편하다.
<br><br>

<h2 id="Concurrent">Concurrent.futures</h2>

```
import concurrent.futures

def ThreadFunction(ThreadIndex:int):
    print("Thread start")

    print(f"Thread number : {ThreadIndex}")

    return ThreadIndex

if __name__=="__main__":

    ThreadCount=10
    ThreadExec=concurrent.futures.ThreadPoolExecutor(ThreadCount)

    for Result in ThreadExec.map(ThreadFunction,range(ThreadCount)):
        print(f"{Result} Thread Done")

    print(f"Thread work has been done")
```

- 사용법은 위 [`ThreadPool`](#ThreadPool) 사용법과 비슷하다.