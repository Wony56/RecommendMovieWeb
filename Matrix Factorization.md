### Matrix Factorization

SVD 활용(
$$
R = P * Q^T
$$
)

row => user (userid x feature(N개))

col => 영화(feature(N개) x movie)



R => 각 유저가 영화에 부여한 평점

F => 장르점수

![제목 없음](C:\Users\multicampus\Desktop\제목 없음.png)

### KNN

* user-based :  feature가 가장 비슷한 user 찾기 (userN에 대한 각 유저의 유사도 측정 )
  * userN이 안본 영화에 대해 가장 비슷한 성향을 가진 유저가 얼마줬는지.. 이사람도 이렇게 줬을것이다라고 predict
* item-based : 영화 별(row) 로 어떤 유저가 봤는지 체크 (col)
  * 해당 영화와 가장 비슷한 similarity 를 가진 영화 찾기 --> 이영화를 다음에 누가 볼것이다라고 예상
* content based : 새영화는 추천했었다는 데이터가 x 
  * ex) 영화별로 어떤 배우가 나온다고 특성을 잡음 ==> similarity 측정 => 유사도가 높으면 추천



ex) m1에 대한 유사도

| user/movie | user1 | user2 | user3 | user4 | similar |
| ---------- | ----- | ----- | ----- | ----- | ------- |
| m1         | 1     | 1     | 0     | 0     | 1       |
| m2         | 1     | 1     | 0     | 1     | 0.71    |
| m3         | 1     | 0     | 0     | 1     | 0.5     |

cosine similarity 



##### 순서

* PCA로 user와 movie idx 차원 축소 (생략가능) ==> scikit-learn에서는 pca대신 svd사용
* 2차원 배열 만들기(각 유저가 각 영화에 얼마의 평점을 줬는지)
* 특성값 조절
* ?값 예측
* 