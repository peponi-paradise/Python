<h1 id="Title">병렬 작업</h1>

- Thread를 사용하는 이유는 주로 병렬 작업 때문이다.
- 아래는 PC에 있는 CPU 카운트를 불러와 병렬 작업을 하는 예시이다.

<details>
    <summary style="font-Weight:bold">  Thread 생성 및 실행, 결과 받아오기 관련 글</summary>
        <p>
        1. <a href="https://peponi-paradise.tistory.com/entry/Python-Threading-Basic" target="blank">Python Threading - 생성 및 기본 사용법</a><br>
        2. <a href="https://peponi-paradise.tistory.com/entry/Python-Threading-Create-Thread" target="blank">Python Threading - Thread를 생성하는 방법들</a><br>
        3. <a href="https://peponi-paradise.tistory.com/entry/Python-Threading-Get-data-from-thread" target="blank">Python Threading - Get data from thread</a>
        </p>
</details>
<br>

<h2 id="DividingJobs">병렬 작업 진행</h2>

```python
from threading import Thread
from multiprocessing import Queue
from os import cpu_count
from time import sleep

def ThreadFunction(ThreadIndex:int,LoopCount:int,ReportQueue:Queue):
    print(f"Thread {ThreadIndex} Work start")

    ## LoopCount만큼 더하기
    ComputingCount=0
    for I in range(LoopCount):
        ComputingCount+=1

    print(f"Thread {ThreadIndex} Work done")

    ## 종료 후 Main thread에 report
    ReportQueue.put((ThreadIndex,ComputingCount))

if __name__=="__main__":

    ## 총 계산 수
    JobLoopCount=100000000

    ## 장착된 CPU의 logical processor 수를 가져온다. (Test system : Intel 10875H 8C 16T)
    WorkerCount=cpu_count()
    print(f"Worker count : {WorkerCount}")

    ThreadReportQueue=Queue()
    ComputingCount=0

    ## 총 계산 수를 Worker 수만큼 나누어 시작
    for index in range(WorkerCount):
        worker=Thread(name=str(index),target=ThreadFunction,args=(index,int(JobLoopCount/WorkerCount),ThreadReportQueue))
        worker.daemon=True
        worker.start()

    ## 모든 Thread 종료 대기
    WorkerDoneCount=WorkerCount
    while True:
        if ThreadReportQueue.empty()==False:

            ReportData=ThreadReportQueue.get()
            print(f"Thread {ReportData[0]} end - Data : {ReportData[1]}")

            ## Thread의 ComputingCount를 더해준다
            ComputingCount+=ReportData[1]

            WorkerDoneCount-=1
            if WorkerDoneCount==0:
                break
        else:
            sleep(0.005)

    ## 모든 Thread 종료 후 최종 ComputingCount display
    print(f"Thread work has been done - Result : {ComputingCount}")
```
<br>

> 작업 결과
>> Worker count : 16
>> Thread 0 Work start
>> Thread 1 Work start
>> ...
>> Thread 9 Work start
>> Thread 3 Work done
>> Thread 2 Work done
>> Thread 10 Work start
>> ...
>> Thread 3 end - Data : 6250000
>> Thread 15 Work start
>> ...
>> Thread 15 end - Data : 6250000
>> Thread work has been done - Result : 100000000

<br>

- 위의 결과와 같이, Thread의 실행 순서가 종료 순서를 보장하지 않는다.
- 따라서 적절한 종료 처리가 필요할 수 있다.
<br><br>