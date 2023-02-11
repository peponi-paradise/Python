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