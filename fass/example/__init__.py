import time
import fass
import fass.information

def ShowProgramInformation()->"显示程序信息":
    print("作者：{}".format(rass.author))
    print("版本：{}".format(rass.version))
    print("联系：{}".format(rass.email))
    print("项目网址：{}".format(rass.url))

def ShowCPUUsage()->"显示 CPU 使用率":
    print(rass.information.CPUMachine())
    while True:
        print("\rCPU使用率：{}%".format(str(rass.information.CPUUsage())), end=' ')
        time.sleep(1)

def ShowMemoryUsage()->"显示内存使用率":
    while True:
        print("\r内存使用率：{}%".format(str(rass.information.MemoryUsage())), end=' ')
        time.sleep(1)
