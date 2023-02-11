<h1 id="Title">Get data from thread</h1>

- Thread에서 가공되는 데이터를 돌려받는 방법은 여러가지가 있다.
- 경우에 따라, 취향에 따라 선택하여 사용하면 될 것 같다.
<br>

<h2 id="global">Global variable</h2>

- Thread는 Process 안에 속하기 때문에, 전역 변수를 사용하는 경우 쉽게 사용할 수 있다.
- 전역 변수인 만큼, 데이터 동기화에 신경 쓸 필요가 있다.
<br>

```
from threading import Thread

# 전역 변수 설정
GlobalVariable=0

def ThreadFunction(LoopCount:int):
    print("Thread start")

    # global 키워드 사용하여 전역 변수 가져옴
    global GlobalVariable

    for I in range(LoopCount):
        GlobalVariable+=1
    print("Work done")

if __name__=="__main__":

    JobLoopCount=10000000

    worker=Thread(target=ThreadFunction,args=(JobLoopCount,))
    worker.daemon=True
    worker.start()
    worker.join()

    print(f"Thread work has been done - Result : {GlobalVariable}")
```
<br><br>

<h2 id="Concurrent">Futures, ThreadPool</h2>

- `Concurrent`의 `futures`, `multiprocessing`의 `ThreadPool`을 사용하는 경우 function에서 return을 받아올 수 있다.[footnote][`Python Threading - Thread를 생성하는 방법들`](https://peponi-paradise.tistory.com/entry/Python-Threading-Create-Thread)[/footnote]
- 아래에 있는 [`Queue`](#Queue), [`Manager`](#Manager)와도 같이 사용할 수 있다.
- 아래는 `futures`의 예시이다.
<br>

```
import concurrent.futures

def ThreadFunction(LoopCount:int):
    print("Thread start")

    ComputingCount=0

    for I in range(LoopCount):
        ComputingCount+=1
    print("Work done")
    return ComputingCount

if __name__=="__main__":

    JobLoopCount=10000000

    ThreadExec=concurrent.futures.ThreadPoolExecutor()
    worker=ThreadExec.submit(ThreadFunction,JobLoopCount)

    ## ThreadFunction의 return이 worker.result()에 들어있다.
    print(f"Thread work has been done - Result : {worker.result()}")
```
<br><br>

<h2 id="Queue">Queue</h2>

- `multiprocessing`의 `Queue`는 FIFO (선입선출) 방식의 Queue다. Thread 생성 시 인자로 넘겨 사용한다.
<br>

```
from threading import Thread
from multiprocessing import Queue

def ThreadFunction(LoopCount:int,ReportQueue:Queue):
    print("Thread start")

    ComputingCount=0
    for I in range(LoopCount):
        ComputingCount+=1
    print("Work done")

    ## 쓰레드 작업 후 Queue에 결과 넣음
    ReportQueue.put(ComputingCount)

if __name__=="__main__":

    JobLoopCount=10000000
    ThreadReportQueue=Queue()

    ## 생성한 Queue를 파라미터로 넣어줌
    worker=Thread(target=ThreadFunction,args=(JobLoopCount,ThreadReportQueue))
    worker.daemon=True
    worker.start()
    worker.join()

    ## 쓰레드 작업 끝난 후 Queue에서 결과 꺼냄
    ReportData=ThreadReportQueue.get()

    print(f"Thread work has been done - Result : {ReportData}")
```
<br><br>

<h2 id="Manager">Manager</h2>

- `multiprocessing`의 `SyncManager`는 `list`, `dict` 등 친숙한 자료형을 사용할 수 있게 해준다.
- [`Queue`](#Queue)와 마찬가지로, 생성 시 인자로 넣어 사용한다.
<br>

```
from threading import Thread
import multiprocessing

def ThreadFunction(InputList:list,InputDictionary:dict):
    print("Thread start")

    InputList.append("Second value")
    InputDictionary.update({"Second key":1})

    print("Work done")

if __name__=="__main__":

    # 공유 자원 생성을 위한 SyncManager 생성
    ThreadReportManager=multiprocessing.Manager()

    # 사용법은 기존 list, dict와 동일
    ThreadList=ThreadReportManager.list()
    ThreadList.append("Initial value")
    ThreadDictionary=ThreadReportManager.dict()
    ThreadDictionary.update({"Initial key":0})

    ## 생성한 List, Dictionary를 넣어줌
    worker=Thread(target=ThreadFunction,args=(ThreadList,ThreadDictionary))
    worker.daemon=True
    worker.start()
    worker.join()

    DataString=""
    for Index in range(len(ThreadList)):
        DataString+=ThreadList[Index]+", "

    DataString+="\r\n"

    for Item in ThreadDictionary:
        DataString+=f"{Item} : {ThreadDictionary[Item]}, "

    print(f"Thread work has been done - Result : \r\n{DataString}")
```
<br><br>