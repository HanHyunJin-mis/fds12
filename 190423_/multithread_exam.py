import threading
# 이건 모듈이다.
n = 1000
offset = n//4

def thread_main(li, i):
    for idx in range(offset * i, offset * (i+1)):
        li[idx] *=2

li=[i+1 for i in range(1000)]
threads=[]

# 스레드를 생성
# 실행 흐름을 담당할 변수를
for i in range(4):
    # Thread는 모듈에 있는 함수이다.
    th=threading.Thread(
        # thread_main에 들어가는 매개변수 li, i
        target=thread_main, args = (li, i))
    threads.append(th)
# 멀티 스레딩
for  th in threads:
    th.start()

# 메인 스레드에서 나머지 스레들 들이 모든 실행을 끝날 때까지 기다린다.
for th in threads:
    th.join()

print(li)
