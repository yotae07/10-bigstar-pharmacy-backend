# 10-bigstar-pharmacy-backend
# Pilly 클론 프로젝트

맞춤영양제 섭취관리 서비스를 제공해주는 Pilly Web site 클론

### 개발 인원 및 기간

- 개발 기간: 2020/07/20 ~ 2020/07/31
- 개발 인원: 프론트엔드 3명, 백엔드 2명

## 팀원

- 프론트엔드: 최준 오호근 박예진
- 백엔드: 이상준 이태성

## 기술 스택 및 구현 기능

### 1. 기술 스택

- Python3, Django, Mysql, Aws(EC2, RDS)

### 2. 협업 툴

- Git, Slack, Notion, Trello

### 3. 구현 기능

- **로그인**(user app)
    - JWT를 이용하여 토큰 생성
    - Bcrypt를 이용하여 비밀번호 암호화
    - 인증 Decorator를 만들어 토큰을 이용하여 통신함
    - 직접 Validation을 만들어 아이디, 이메일, 전화번호, 비밀번호 검증(실패)

- **설문조사**(survey app)
    - 사용자의 답변에 따라 질문이 나오게 API 구현
    - 미리 DB에서 Answer에 tag라는 colum으로 다음 질문 아이디를 표시해둠

## 프로젝트 후기

[프로젝트 후기](https://velog.io/@yotae07/1%EC%B0%A8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%9B%84%EA%B8%B0)

## 프로젝트 결과물 영상

[프로젝트 결과물 영상](http://asq.kr/FSzLFOGKdKYl)
