<h1 id="Thread">Thread</h1>

- 작업을 병렬로 수행하기 위해 사용한다.
<br>

<h2 id="BasicFunctions">Basic Functions</h2>

```
## Import 항목
from threading import Thread

## 생성자
Thread(target="Target function want to call", name="Thread name", args=("Parameter","Want","To Use"))

## Daemon 설정 (Background thread)
Thread.daemon=True

## Thread start
Thread.start()

## Thread alive check
Thread.is_alive()

## Wait for Thread end
Thread.join()
```
<br>

- 위 항목 중 daemon 플래그의 경우, `C++` 또는 `C#`의 백그라운드 쓰레드와 같다. True로 설정 시, 상위 쓰레드 또는 프로세스 종료 시 바로 동작이 중지된다.

> Thread object in docs.python.org[footnote][Python - Thread](https://docs.python.org/ko/3/library/threading.html#thread-objects)[/footnote]
>> 종료 시 데몬 스레드는 갑자기 중지됩니다. 그들의 자원(가령 열린 파일, 데이터베이스 트랜잭션 등)은 제대로 해제되지 않을 수 있습니다. 스레드가 우아하게 중지되도록 하려면, 스레드를 데몬이 아니도록 만들고 `Event`와 같은 적절한 신호 메커니즘을 사용하십시오.

<br>

<h2 id="BasicUse">Basic Use</h2>

```
from threading import Thread
from time import sleep

def ThreadFunction():
    print("Thread created")
    print("Work start")
    print("Working...")
    sleep(1)
    print("Work done")

if __name__=="__main__":

    worker=Thread(target=ThreadFunction)
    worker.daemon=True
    worker.start()
    worker.join()
    print("Thread work has been done")
```
<br>

> 실행 결과
>> Thread created<br>Work start<br>Working...<br>Work done<br>Thread work has been done

<br><br>