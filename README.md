# Big Data 2주차 프로젝트

## SHEEPCHA

### 1. 주요기능

- 로그인/회원가입

  ![1567746700359](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\1567746700359.png)

  ![1567746713574](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\1567746713574.png)

- 관리자페이지 (http://localhost:8080/admin 으로 접속) 

  ![1567746079973](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\1567746079973.png)

  ![1567746131894](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\1567746131894.png)

- 영화 검색 기능( 연령대/직업군/성별 기준으로 검색 가능 & 정렬 가능)

![1567746671729](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\1567746671729.png)

- 영화 상세페이지
  - kmeans 클러스터링을 활용하여 유사영화 뽑아 보여줌

### 2. 프로젝트 실행(Terminal)

- Frontend

  frontend 디렉터리에서 **npm run serve** 입력

- Backend

  backend 디렉터리에서 **python manage.py runserver** 입력