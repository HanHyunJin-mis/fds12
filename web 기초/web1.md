programming : 프로그램을 만든다
프로그램 : 해야할 일의 순서
웹 프로그래밍 : 브라우저에서 돌아가는 프로그램
웹을 통해 이용하는 프로그램을 만든다.

인터넷이 어떻게 작동되는지
internet - inter network
lan끼리 연결된 것이 wan, wan을 연결한 것이 인터넷
문서를 주고받기 위해 생겨남

프로토콜

광케이블


1.브라우저 요청
2. hosts 파일 검색
3. DNS 서버 검색 (전화번호부)
4. 해당 주소로 연결

내가 자주 가는 사이트의 경우 1 - 2 - 4


http = scheme - 어떻게
logo-logos.com - 어디에
path - 무엇을


http
https - 암호화, 누구나 암호화 할 수 있지만 보는 건 나 하나
mailto - 메일 교환 프로토콜
ftp - file transfer protocol

<schme>://<name>:<pwd>@<host>:<port(ex. 차선)>/<path>;<parameter(잘 안씀)>?<query>#<fragment(클릭시 페이지 내의 지정 위치로 이동)>
:// - 뒤에 아이디와 패스워드 방식을 쓸 수 있는 것
한 프로그램은 한 port만 사용
?가 끝나면 뒤에 query string이 붙는다.

URI(특정 리소스의 구분자, ex. 주민번호)
URL
URN(특정 리소스의 이름)

http : hyprttext - 문서와 문서를 연결하는


http 1 - 주고받는 형식
http 2 - 한꺼번에 주고받는 형식, 무조건 https 통신

MIME - 이메일 전송 표준 프로토콜
사진 확장자는 변경이 가능하다. 정확하게 그 파일인지 알 수 없음

메소드 방식 (어떤 의도로 접근하는지 알 수 있음)
get : 리소스 획득
put : 리소스 저장
delete : 리소스 삭제
post : 데이터 전송
head : http 헤더 획득

put과 post가 구분되어 있지만 구분해서 쓰지는 않음

http는 메세지 단위로 주고받음

메세지 : 시작줄, 헤더, 본문

TCP(전송 계층)/IP(네트워크 계층)
TCP : 데이터 손실이 되지 않음
UDP : 데이터 손실을 허용

server의 구성
로딩 최적화, 이미지 파일 관리 중요

web server : 사용자가 많을 경우, 이미지 파일 손상 가능
D.B server : 고객 데이터, 자주 꺼내는 데이터도 저장해놓음
image server 
cache server : CDN 미국의 동영상을 사용자가 봤을 경우 한국의 cache server에 저장 (미리 하나의 파일로 저장, 서버를 늘리는 것보다 저렴, 유용)





예쁜 사이트 베껴보기
