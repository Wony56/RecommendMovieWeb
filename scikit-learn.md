`pip install -U scikit-learn`



## K-Means

군집화에서 활용되는 기본 알고리즘

grouping 한다.

K개로 군집한다. 유사한 입력 값끼리 묶어서 군집을 찾습니다. 굉장히 클리어한 알고리즘

목적 함수 값이 최소화 될때까지 클러스터의 중심 위치와 각 데이터가 소속될 클러스터를 반복해서 찾는다.

임의의 중심값 k개를 고름

중심에서 각 데이터까지의 거리를 계산

각 데이터에서 가장 가까운 중심을 선택하여 클러스터 갱신

정해진 중심을 가지고 계속 반복하면서 똑같은 상황이 유지되면 종료

```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3).fit(data)
# n_clusters -> 몇 개로 군집화
kmeans.labels_ # 각 데이터에 대한 클러스터 결과물

```

