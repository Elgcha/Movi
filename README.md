# 특화 프로젝트 IoT 제어

## 목차

1. [카테고리](#카테고리)
2. [프로젝트 소개](#프로젝트-소개)
3. [팀 소개](#팀-소개)
4. [주요 기능](#주요-기능)
   1. [인지](#인지)
   1. [자율주행](#자율주행)
   2. [Web](#web)
      1. [메인페이지](#메인페이지)
      2. [상세페이지](#상세페이지)
      3. [로봇페이지](#로봇페이지)
      4. [알림페이지](#알림페이지)

## 카테고리

| Application | Domain | Language | Framework |
| ---- | ---- | ---- | ---- |
| :white_check_mark: Desktop Web | :white_check_mark: AI | :white_check_mark: JavaScript | :white_check_mark:Vue.js |
| :black_square_button: Mobile Web | :black_square_button: Big Data | :white_check_mark: TypeScript | :black_square_button:React |
| :white_check_mark: Responsive Web | :black_square_button: Blockchain | :black_square_button: C/C++ | :black_square_button: Angular |
| :black_square_button: Android App | :white_check_mark: IoT | :black_square_button: C# | :black_square_button: Node.js |
| :black_square_button: iOS App | :black_square_button: AR/VR/Metaverse | :white_check_mark: Python | :white_check_mark: Flask/Django |
| :black_square_button: Desktop App | :black_square_button: Game | :black_square_button: Java | :black_square_button: Spring/Springboot |
| | | :black_square_button: Kotlin | |

---

## 프로젝트 소개


![Logo](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/b71a9d785a2a244fe3cf7cde84f9aca3/Logo.png)

* 프로젝트명: MOVI
* Description
  * IoT, 인공지능, 자율주행을 이용한 택배 자동 분류 로봇
* 사용 기술
  * IDE
    * VSCode
  * Frontend
    * VueJs3 with TypeScript
    * Element Plus
    * vite
  * Backend
    * Django
    * Python-socketio
  * DB
    * sqlite3

## 팀 소개

* 김남훈: 팀장, 인지
* 이규은: 인지
* 박홍규: 인지
* 이진행: 자율주행
* 이진희: 자율주행(Mapping, UCC)
* 전건하: Web

## 주요 기능

### 인지

### 자율주행

### Web

* 시뮬레이터가 작동하는 상황을 보고 관리하는 페이지. 관리자 및 택배 기사들이 사용하는 것을 가정
* 웹소켓을 통해 시뮬레이터와 통신

#### 메인페이지

- 관리자의 경우 전체 자료, 택배 기사의 경우 자신의 자료가 표시 됨
- 왼쪽 버튼을 통해 볼 자료를 선택 가능
- 지역 검색을 통해 특정 지역의 자료만 표시 가능

![메인](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/dd7c55d1fea4798169f901cd359fafe2/%EB%A9%94%EC%9D%B8.png)

![메인2](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/12f166ca4ca0b8c91fea60ab2f71d05f/%EB%A9%94%EC%9D%B82.png)

- 모바일로 볼 때 화면

![메인_m1](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/688b90b29140653646098259eb381b1a/%EB%A9%94%EC%9D%B8_m1.png)

![메인_m2](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/88f073babd8218c9e59f56cfff26f46b/%EB%A9%94%EC%9D%B8_m2.png)

#### 상세페이지

- 택배들의 정보를 볼 수 있음.

![상세](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/be97444d3d4feed61edb65a30c6fb05c/%EC%83%81%EC%84%B8.png)

![상세m](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/6c38f1738b24c82f9d25826952ac8354/%EC%83%81%EC%84%B8m.png)

#### 로봇페이지

- 현재 로봇들의 상태 확인 가능

  ![로봇](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/886e6f8cfd98efda18fca2332cb90f8f/%EB%A1%9C%EB%B4%87.png)

![로봇m](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/9c19ed0ae9aee0ddbe8414ba1f97462b/%EB%A1%9C%EB%B4%87m.png)

#### 알림페이지

![알림1](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/113cf2aeb4922b3d21d9a03b3f1cdf42/%EC%95%8C%EB%A6%BC1.png)

![알림](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/cf38db288a408715d37a0cd5012f061a/%EC%95%8C%EB%A6%BC.png)

![알림_m](https://lab.ssafy.com/s06-iot-control-sub2/S06P22A501/uploads/d2e41ad863098ce2ff0302811ba3f65e/%EC%95%8C%EB%A6%BC_m.png)

[위로](#목차)

- 물류 택배를 분류하는 시설물 안전 점검 로봇
  > > > > > > > bf991eacfe67174fde94f973c2f3708fdb24d9e1
