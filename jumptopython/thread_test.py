import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다

def long_task():    #5초의 시간이 걸리는 함수 
    for i in range(5):
        time.sleep(1)   # 1초간 대기한다. 
        print("working:%s\n" % i)

print("Start")


threads = []

for i in range(5):
    t = threading.Thread(target=long_task) # 스레드를 생성한다. 
    threads.append(t)

for t in threads:
    t.start()  # 스레드를 실행한다 

for t in threads:
    t.join() 

print("End")