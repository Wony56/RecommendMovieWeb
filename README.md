# Big Data 3주차 프로젝트

## SHEEPCHA

### - 주요기능
1. 로그인 / 회원가입
    - user + "숫자"를 아이디와 비밀번호로 하여 로그인하면 됩니다.
    - 회원가입을 완료하면 자동 로그인되며 구독페이지로 자동으로 이동되게 됩니다.

    <img src="./image/entrance.png" width="50%">
    <img src="./image/signup.png" width="50%">
    <img src="./image/home.png" width="50%">
2. 구독페이지
    - 랜덤으로 보여주는 영화목록들에 대해 평점을 부여할 수 있으며 최소 10개이상 부여할 경우 구독 버튼이 생깁니다.
    - 구독페이지에서 부여한 평점데이터들을 기반으로 최초가입자에게 영화 추천을 해주도록 하였습니다.

    <img src="./image/subscribe.png" width="50%">
3. 영화검색
    - 웹 페이지 상단의 헤더바에 있는 검색창을 통해 검색이 가능합니다.
    - 아무 기입없이 엔터를 치면 전체 영화 검색이 진행되고, 특정 키워드를 입력하면 키워드가 제목에 포함된 영화들을 검색해줍니다.
    - 검색 페이지에서 조회수/평점/성별/직업별/연령별로 정렬이 가능합니다.
    - 영화 카드를 하나 누르면 해당 영화의 상세페이지가 뜹니다.

    <img src="./image/search.png" width="50%">
4. 영화상세페이지
    - 해당 영화의 평점을 등록 및 수정할 수 있습니다.
    - KMeans알고리즘 기반으로 유사한 영화들을 하단에 표시하였습니다.

    <img src="./image/movie_detail.png" width="50%">
5. 프로필
    - 로그인한 사용자의 신상정보, 관람한(평점을 준) 영화목록, 빅데이터를 기반으로 학습한 데이터를 기반으로 사용자 추천 영화 목록을 보여줍니다.
    - 구독 여부에 따라 추천 영화목록을 표시하였고, 구독은 기간연장 버튼을 눌러 구독을 신청할 수 있습니다.

    <img src="./image/user_detail.png" width="50%">
6. 관리자페이지
    - id: admin / pwd: admin으로 로그인 후 http://localhost:8080/admin 으로 접속.
    - 사용자 정보와 영화정보를 한눈에 파악할 수 있으며 관리자가 유저정보와 영화정보를 수정 또는 삭제할 수 있습니다.

    <img src="./image/admin1.png" width="50%">
    <img src="./image/admin2.png" width="50%">
