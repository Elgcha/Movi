# Back - Django

* 가상환경 생성

```
python -m venv venv
```

```
source venv/Script/activate
```

* 환경 구성

```
pip install -r requirements.txt
```

```
python manage.py migrate
```

* 서버 실행

```
python manage.py runserver
```



# 패치노트

## 04/04

* 웹소켓 통신을 통한 로봇, 택배 상태 변화 함수 작성

## 04/01

* socket io, eventlet을 이용한 웹소켓 서버 구성 - socketio_app, server/wsgi.py

## 03/29

* robots app 추가

## 03/28

* 모델 변경 - fname, tname 삭제

## 03/15

* 지역별 검색 시 사용할 db에 저장된 주소 반환 api 추가

## 03/10

* 상세페이지 검색 기능 구현 (지역, 배송기사, 송장 번호)
* 메인페이지 검색 기능 구현(지역, 배송기사)
* 메인페이지 조회 api 구현

## 03/09

* 택배 리스트 조회 api 구현, 페이지네이션 추가
* 직렬화에서 Delivery와 Category는 1:n 구조인데 many=True로 되어있던 것 수정

## 03/08

* Back(Django) 기본 구조 생성
* JWT 토큰을 이용한 회원가입, 로그인 기능 구현
* 개인정보 수정 기능 구현
* db에 택배 추가 기능 구현