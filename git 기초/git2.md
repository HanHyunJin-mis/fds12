# Commit하고 수정하기

### 초기 설정
```
git config --global user.name "유저 "
git config --global user.email "가입 이메일"
git config --global core.editor "vim"
git config --list 
```

## Commit 과정
`git init`  - 보내는 사람의 주소만 입력한 꼴


`rm -rf .git` 을 입력하면 git으로 가는 것이 사라짐


```
git 관련한 명령어는 모두 git으로 시작한다.
``` 
***

`git remote add cat https://github.com/HanHyunJin-mis/very_first_repo.git`

`git remote` - 받는 사람 이름(별명)

```
나의 git 주소를 cat이라는 이름으로 연결

git remote add(받는 사람 주소를 송장에 추가해라) + 별명(cat) + 주소
```

***
`git remote remove cat` - cat을 git에서 삭제해라

`git remote get-url cat` cat의 주소를 알려달라는 말



`vim` 이랑 `vi` 랑 같음

`vi index.html` 은 vim으로 index.html 열기

***
### index.html을 git에 올리기

`git add index.html`
`git commit`
`git push -u cat master`

`git status` 로 상태 틈틈히 확인


- 작업 내용을 잘못 올렸을 때
`git rm --cached index.html` 은 깃에 커밋한 파일을 삭제


`파일이름` Feat : Add index.html
`부가 설명`  I added index.html to practice git. And I am a brilliant Developer.


***
## Commit 파일 수정

(가급적이면 사용X)
git add . (모든 부분 수정)

feat : edit index.html (add head, body)
html tags.I add head body.
