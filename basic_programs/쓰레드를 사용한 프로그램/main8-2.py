#메인코드가 동작할 때만 쓰레드 동작 코드
import threading
import time

def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)

t1 = threading.Thread(target = thread_1)
#thread를 daemonthread로 설정하여 메인동작이 실행될때만 실행되도록 설정
t1.daemon = True
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0)