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