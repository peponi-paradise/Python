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