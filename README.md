# 10-bigstar-pharmacy-backend
# Pilly 클론 프로젝트

맞춤영양제 섭취관리 서비스를 제공해주는 Pilly Web App 클론

### 개발 인원 및 기간

- 개발 기간: 2020/07/20 ~ 2020/07/31
- 개발 인원: 프론트엔드 3명, 백엔드 2명

## 팀원

- 프론트엔드: 최준 오호근 박예진
- 백엔드: 이상준 이태성

## 기술 스택 및 구현 기능

### 1. 기술 스택

- React, React-Router, Fetch API, Sass

### 2. 협업 툴

- Git, Slack, Notion, Trello

### 3. 구현 기능 상세 설명

- **로그인**
  - UI 구현
  - fetch API로 로그인 기능 비동기 처리
  - 로컬스토리지 사용해서 JWT 활용
  - 소셜로그인 기능 구현

## 작업순서

1. `git checkout master`: 마스터 브랜치로 이동
2. `git pull origin master`: github에 변화된 최신 코드를 받아온다
3. `git branch feature/name`: 본인의 브랜치 생성
4. `git checkout feature/name`: 브랜치로 이동
5. `git merge master`: 마스터에서 받아온 최신 코드를 브랜치에 병합시킨다
6. `npm install`: package.json dependencies 에 추가된 모듈 로컬에 다운로드
7. 최대한 기능별로 쪼개서 작업하기
8. 프로젝트 상위 디렉토리로 가서 `git add .` 명령어로 내가 수정한 코드를 git stage 에 올린다
9. `git status`: add가 잘 되었는지 확인
10. `git commit -m "commit message"`: commit message는 팀원과 상의한 후에 slack 에 공유한다
11. `git push origin feature/name`: 본인 브랜치에서 작업한 내용을 원격 리포지토리에 올린다
