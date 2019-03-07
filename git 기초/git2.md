# Git에 파일 올리기, 수정, 삭제

### 초기 설정
```
git config --global user.name "유저 "
git config --global user.email "가입 이메일"
git config --global core.editor "vim"
git config --list 
```

<img src="/images/Git.png" width="75%">

<br>

## Commit 과정
`git init`  - 보내는 사람의 주소만 입력한 꼴


`rm -rf .git` 을 입력하면 git으로 가는 것이 사라짐


```
git 관련한 명령어는 모두 git으로 시작한다.
``` 
<br>

`git remote add cat https://github.com/HanHyunJin-mis/very_first_repo.git`

`git remote` - 받는 사람 이름(별명)

`git clone` + 주소 + 주소에 있는 파일을 복사할 폴더 이름 - git 내에 파일이 존재할 경우 입력 

```
나의 git 주소를 cat이라는 이름으로 연결

git remote add(받는 사람 주소를 송장에 추가해라) + 별명(cat) + 주소
```

<br>

`git remote remove cat` - cat을 git에서 삭제해라(very_first_repo라는 저장소의 주소를 대신한 cat이라는 이름을 삭제하는 것)

`git remote get-url cat` cat의 주소를 알려달라는 말



`vim` 이랑 `vi` 랑 같음

`vi index.html` 은 vim으로 index.html 열기

<br>

### index.html을 git에 올리기

1. `git add index.html`

2. `git commit`

3. `git push -u cat master`

4. `git status` 로 상태 틈틈히 확인


- 작업 내용을 잘못 올렸을 때
`git rm --cached index.html` 은 add한 파일을 unstrage하는 것


`파일이름` Feat : Add index.html

`부가 설명`  I added index.html to practice git. And I am a brilliant Developer.


<br>

## Commit 파일 수정

(가급적이면 사용X)
git add . (수정된 모든 파일을 add하는 것)

feat : edit index.html (add head, body)

html tags.I add head body.

<br>

## Commit 파일 삭제
`rm index.html` - 내 컴퓨터에서 파일 삭제

`git add index.html` - git에다 삭제했다는 것을 add함

`git push -u cat master` - git에다 삭제했다는 것을 push
