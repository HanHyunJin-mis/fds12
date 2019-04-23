#스레드를 50개를 만들고 각 스레드가 +1씩 100만번을 하도록 만듬
import threading

# 공유 자원
# 모든 스레드에서 접근이 가능한 자원
# 전역 변수

g_num = 0
# lock 개체
lock = threading.Lock()


def thread_main():
    global g_num

    # critical section - 오직 단 하나의 스레드만 접근할 수 있다.
    # 임계 영역
    # 어떤 스레드에서 공유 자원에 접근한 후 수정, 변경 하려는 코드 -> 외부에 전역변수로 lock 개체를 만들면 된다.
    lock.acquire()
    for _ in range(100000):
        g_num +=1
    lock.release()

threads=[]

for _ in range(50):
    th=threading.Thread(target= thread_main)
    threads.append(th)

for th in  threads:
    th.start()

for th in  threads:
    th.join()

print('g_count : {:,}'.format(g_num))
