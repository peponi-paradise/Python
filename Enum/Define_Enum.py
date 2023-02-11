from enum import Enum

class SWActionEnum(Enum):
    READY=0
    IN_PROGRESS=1
    AIPROCESS_END=2

class ProgressEnum(Enum):
    AIProgress_None=0
    AIProgress_LoadModules=20
    AIProgress_LoadFile=40
    AIProgress_SetDataArray=60
    AIProgress_AITraining=80
    AIProgress_AIProcessResulting=90
    AIProgress_Success=100
    AIProgress_Failed=99

class DataFileTypeEnum(Enum):
    EXCEL=1
    CSV=2
    NONE=9999

class Color(Enum):
    LightGray=0
    SkyBlue=1
    MediumSeaGreen=2
    DarkOrange=3
    Crimson=4