# final-pjt
금융 상품 비교 애플리케이션

### 개발 일지

|No|일자|이름|내용|
|:---:|:---:|:---:|:---:|
|1|23/11/15|백지윤|vue - 메인페이지/회원가입/로그인/로그아웃 구현, 환율계산기 |
|2|23/11/15|배민지|django - 메인페이지/로그인/로그아웃/ 구현, 환율계산기|
|3|23/11/16|백지윤|vue - 커뮤니티 생성, 디테일, 수정, 삭제 구현, 정기 적금 페이지 생성 django - board 수정/ serializer 생성|
|4|23/11/16|배민지|django - 정기 예금 사이트 만들기, currency 생성, 예적금 금리 비교(데이터 저장, 전체 조회, 상세조회)|
|5|23/11/17|백지윤|vue - 커뮤니티 생성, 디테일, 수정, 삭제 구현, django - board 수정/ serializer 생성|
|6|23/11/17|배민지|django -  예적금 필터링 기능 구현, 은행 데이터베이스 생성, 환율 계산기 생성|
|7|23/11/20|백지윤|vue - 커뮤니티 댓글 구현, 예적금 구현|
|8|23/11/20|배민지|django -  환율계산기 수정, 은행 db 수정, 유저 모델 수정, 유저 프로필 차트 구현|
|9|23/11/21|백지윤|vue - 예적금 필터링, CSS |
|10|23/11/21|배민지|vue -  환율계산기 수정|
|11|23/11/22|백지윤|vue- 예적금, 가입 후 db에 저장|
|12|23/11/22|배민지|vue, django -  환율계산기 수정(원화 변환 추가), 프로필 차트 렌더링, 유저정보 수정기능|
|11|23/11/23|백지윤|알고리즘. UI 디자인 최종|
|12|23/11/23|배민지|알고리즘|



# **1. 프로젝트 개요**

> **사용자 맞춤 금융 추천 웹 FREDDIT**
> 

<FREDDIT>은 예금과 적금 상품이 신속한 비교와 추천 기능을 사용자에게 제공하며, mbti 및 사용자별 금융상품을 추천하는 사용자 친화적 금융 추천 웹사이트입니다.

# 2. 주요 기능

## 2.1 홈


- NavBar를 구현해 홈에서 각각의 페이지로 navigate할 수 있으며, 로그인과 회원가입을 진행할 수 있습니다. 
- 기본적인 웹에 대한 소개를 위해 호버 및, 애니메이션을 css를 통해 구현했습니다.

<img src='../final-pjt//final-pjt-front/src/assets/img/main/home.gif'>

## 2.2 정기 예금,적금

- 기본적인 적금, 예금 정보를 프론트엔드 단에서 for each문을 통해 개월수, 은행 이름으로 구분해서 구별하였습니다.
- 사이드바 구현을 통해 정기 예금, 적금 상품을 확인할 수 있습니다.

<img src='../final-pjt//final-pjt-front/src/assets/img/main/정기예금적금.gif'>

## 2.3 환율계산기

- 환율 계산기를 통해, 자국 화폐에서 각 나라별 화폐로 환율을 계산할 수 있습니다.

<img src='../final-pjt//final-pjt-front/src/assets/img/main/환율계산기.gif'>


## 2.4 지도 보기

- 카카오 지도 api를 이용해, 지역을 선택후 , 해당 은행을 선택할 시 은행의 위치를 보여줍니다.


## 2.5 mbti 성향 설문 체크

- 간단한 설문지를 라디오 버튼을 이용해 UI를 구성하였고, 해당 번호에 맞는 mbti 성향을 체크하여 본 설문지를 통해 간단하게 mbti를 체크후, 해당 성향을 통해 mbti별 TOP100 금융상품을 추출하여, 상품을 추천하였습니다.

<img src='../final-pjt//final-pjt-front/src/assets/img/main/투자성향.gif'>

---

# 6. 팀원 소개

|![지윤](https://avatars.githubusercontent.com/u/94150712)|![민지](https://avatars.githubusercontent.com/u/139304989)|
|:---:|:---:|
| [백지윤](https://github.com/1234jienf) <br> Frontend | [배민지](https://github.com/MJBae327) <br> Backend |

