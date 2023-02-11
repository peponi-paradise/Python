<h1 id="title">Python - Define Enum</h1>

<h2 id="intro">Introduction</h2>

1. `Python`의 경우 `C++`, `JAVA` 등과는 달리 enum (열거체)를 기본적으로 지원하지 않는다.
2. `Enum`이 필요한 경우, enum 모듈의 Enum 클래스를 상속받아 사용할 수 있다.
3. 새롭게 정의한 `Enum 클래스`는 Property `name` 및 `value`를 통해 이름과 값을 확인할 수 있다.

<br><br>

<h2 id="code">Code</h2>

```python
from enum import Enum

class AIProgress(Enum):
    AIProgress_None=0
    AIProgress_LoadModules=20
    AIProgress_LoadFile=40
    AIProgress_SetDataArray=60
    AIProgress_AITraining=80
    AIProgress_AIProcessResulting=90
    AIProgress_Success=100
    AIProgress_Failed=9999
```

<br><br>

<h2 id="example">Use example</h2>

```python
progress=AIProgress.AIProgress_LoadModules
print(progress.name)
print(progress.value)
```