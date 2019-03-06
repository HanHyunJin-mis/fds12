html 기초

<!Doctype html>을 쓰지 않으면 브라우저가 html의 예전 버전으로 인식 (브라우저마다 다르게 보인다.)

html 태그에서 정교한 형식을 쓰는 이유
브라우저, 검색엔진이 해석할 수 있게 해줌

sementic web - 내가 원하는 웹을 걸러내서 찾아주는 웹

head : 브라우저에서 가져가야 하는 정보

title : 제목

rander: 화면을 그린다.

html은 요소로 구성되어 있고 tag로 표시한다.

container, empty

<>안에 내용을 담을 수 있는 태그<>
<!-- 컨테이너 태그, 홈태그>

대부분이 컨테이너 태그, 짝태그
<img src ="logo.png">
<!-- empty 태그, 홈태그>

모르는 태그를 찾을땐 w3school, stackoverflow에서 찾기, how to(많이 사용), what is : 많이 검색해보기

inline : 한 줄에 여러 개의 요소가 같이 있을 수 있다. 크기를 갖지 않는다.
block : 한 줄에 하나의 요소만 들어간다. 크기를 갖는다. 사용자가 크기 조절 가능

주요 태그

css가 빠지더라도 구성이 흐트러지지 않게 짜는 것이 중요
html : 문서의 시작
head : 문서 정보 블록 title, meta, link 등을 포함
body : 렌더링 될 영역의 시작
table : 구성이 잘 흐트러지지 않아서 추천
div : division 공간
h1 : heading 제목
a : anchor 링크
p : 문단
form : ! 중요, 입력 태그 - input textarea (사용자의 입력을 받음)


주요 속성
<span data-'custom 속성값' = "">
name : form, iframe, input 등 (back-end와 소통)
width : block, inline-block(inline에서 높이, 크기 조절 가능) 등
height : block, inline-block 등
type : input, link, script, style
href : a, link
value : input(html5부터는 커서를 누르면 지워짐), option
src : lmg, video,audio, embed, iframe, script

<!doctype html>
strict : 정해진 양식에서 벗어나면 error 출력
transitional : html4 양식을 지원하겠다.
doctype이 아예 없으면 html4의 하위버전으로 인식

하위버전 문서도 준비하면 좋음
<html lang = "ko" : 사용할 언어 ISO 코드
다국어 지원 : 위치에 따라 언어 코드를 바꿔주는 것
국가지원사업 : 사용성 평가 점수를 매기기 때문에 필요한 요구를 알아두는 것이 좋음

위지위그 에디터 : 평소에 찾아보기
award 참여해보기
오류 만들어보기
태그와 css를 연관지어서 적기
명확한 이유와 맞는 방법을 생각해보기

