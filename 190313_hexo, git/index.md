.gitignore는 내가 받고 싶지 않은 파일형태
#cusotom이라는 주석을 달고 추가 명시

*.py 
hidden/* - hidden이라는 폴더 안의 모든 파일
java/*.java - 자바라는 폴더의 모든 자바 파일

파일이 들어있긴 하지만 올라가진 않음

hexo init blog
npm install
hexo new post "How to start hexo"

브랜치

branch - 분기점을 생성하고 독립적으로 코드를 변경할 수 있도록 도와주는 모델

비선형 작업 - 특정한 기점을 분기로 쳐서 각자 개발하는 것(끝나는 대로 합침)
분기점을 형성하는 것을 브랜치를 생성한다는 것
git branch -r
git branch -a
*이 내가 지금 위치해 있는 공간
공간
git branch feat/index-edit
git checkout - 브랜치 이동

병합 git merge 브랜치명

시간
git checkout 'c92e2de351b1b3c6a2eaadd32720de3753636a64'

Hexo
node js, git 설치 필수
node js 버전에 따라 실행되지 않을 수 있다.
window는 git bash에서 작업 안될 수 있음

npm install -g hexo-cli 헥소 설치
hexo --version 헥소 버전확인
init blog - 블로그(파일) 생성
cd blog (블로그 이동)[블로그 안에서 해줘야 함]
npm install npm 설치
npm install hexo-deployer-git --save
hexo new port "title"
hexo generate
hexo server 서버 확인
hexo deploy

업로드 할 때
hexo new port "title"





