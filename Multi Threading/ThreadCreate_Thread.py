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