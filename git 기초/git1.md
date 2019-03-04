# Git 기초 - shell command
## 최우영 강사님 블로그
`
http://www.ulgoon.com/
`

at&t
데니스 리치, 켄 톰슨
리차드 스톨먼 - GNU 프로젝트
gnu에는 커널이 없엇다

리눅스
리누스 토발즈가 개발

shell의 시작
 - zshell
 - bash

# Git bash

`~` - 우리의 현재 위치 

`$` - 입력준비가 되었다는 뜻 

`여러명의 유저도 접속 가능` - 사용자에 따라 다른 화면을 보여줌 

`ls` - 파일과 폴더의 리스트가 나온다 

`-` 로 옵션을 붙임(ls 뒤에) 

`-a` 는 숨김 파일까지 모두 보겟다. 

`-l` 은 한줄씩 모든 정보를 보겠다. (옵션의 조합 가능) 

`clear` 창 정리 - 모두 삭제 
 
내 위치를 이동할 때는 cd 사용
상단으로 올라갈 때는 .. 입력
그냥 cd  or cd~ 만 치면 유저의 최상단으로 올라감

## 파일 생성
`touch` 사용

```
ex : touch index.css
```
## 폴더 생성
`mkdir + 폴더 이름` 사용


## 객체 이동 
`- move(mv)` 사용

어떤 파일을 어디로 옮겨라 라는 구조

ex : mv index.html ..

`mv index.html dev` - dev로 파일 이동

## 복사하다 
`- clone, duplicate, copy`
`copy(cp)` 사용
```
copy는 이름을 바꾸면서 복사도 가능
```
`cp index.html dev/index2.html`

`cp blahblah.html blahblah2.html`

### rename 
`mv` 사용

`mv index2.html blahblah.html`

## 삭제하다 
`- remove(화학적) delete(물리적) eliminate pop`
`r

`rm blahblah.html`

## 폴더 지우기
`rm -r dev`
```
dev라는 폴더를 지우기 - 내가 폴더 내에 있는 경우에는 지울 수 없다.
```

ps. \t, \n, # - hashtag, ^ - carot, * - asterisk, ' " `, ~ - tilled

```
절대 경로 보기 - pwd

python으로 hello.py를 열어라
python hello.py
```

## vim command
vim은 모드가 존재
처음 킬 때 나타나는 것은 normal 모드
글자를 입력하기 위해서는 insert 모드(사용자의 입력을 받음)로 들어가야 한다. (i를 입력)
d는 잘라내기 p는 붙여넣기 shift + y는 복사하기
:q! - 저장안함
:wq - 저장하고 나감
작성하다 그냥 껐을 경우에는 해당 파일(swp) 삭제

sudo?
rm -rf/ 하면 모든 것이 지워진다.
wsl?

