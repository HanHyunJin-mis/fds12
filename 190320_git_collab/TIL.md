# git flow
    1. git flow init - git 초기화
        - 총 5가지 설정을 해주는데 window에서

<img src="/images/git_flow.jpg" width="75%">
        master : 최종 릴리즈한 안정화 버전
        develop : 다음 릴리즈를 위해 개발중인 최신 버전
        feature : 특정 기능 개발을 위한 branch
        release : 릴리즈 점검을 위한 branch
        hotfix : 긴급 버그 픽스를 위한 branch
        support : 버전 호환성 문제 처리를 위한 branch
			git flow feature start + branch_name
			git add files : touch + file_name
			git add, commit, push
			git flow feature finish + branch_name
			cd .. and git merge branch_name
    git remote -v를 통해 git remote의 이름과 주소를 한번에 확인할 수 있다.

