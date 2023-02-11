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