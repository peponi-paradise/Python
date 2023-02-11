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