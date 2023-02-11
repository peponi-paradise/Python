## import 항목
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