프로젝트 내에서 파일 이동을 할 때 - 파일의 연속성을 위해
git mv README.md handouts/ : git으로 넣어랏

개발용 브랜치 배포용 브랜치로 나뉜다.

git flow init - 이름 정할 수 있다.
나온 브랜치에서 push하지 않고 커밋, merge하면 local에서는 브랜치가 삭제됨, remote에서 흔적이 남음

git flow feature start 브랜치명 -> 브랜치로 이동

git add
git commit -m "feat: add readme.md
I add readme.md to practice git, git-flow
"
git push origin css-edit
git flow feature finish readme-edit

버전관리, 테스트
git flow release start v.0.0.1.00190320001
git flow release finish v.0.0.1.00190320001

협업용 repo 생성 (git flow init 포함)
feature/project-init 브랜치 생성 후 
index.html 생성, develop에 merge
fork
merge

1. clone
2. git remote add rmorigin pm의 주소
git remote get-url rmorigin
3. git fetch rmorigin develop -> fetch 일단 받아두는 것
4. git merge rmorigin develop -> 지금 있는 나의 develop의 브랜치와 merge (push전에 항상 확인)
5. git push origin develop - develop branch를 origin(내 gith) 서버에 push
