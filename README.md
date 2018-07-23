# SnuttleGA
Snuttle project for Genetic Algorithm based on Xiang's papers

## Classes

1. Chromosome
>운행 정보를 가지고 있는 유전자(Station n개에 해당하는 유전자의 길이는 2n) - 논문 참고

2. Pool
>Chromosome의 배열을 가지고 있다.
>Evolution 과정을 담당하도록 한다. Local Optimization도 한다.
>Pool을 여러개 만들어서 여러개의 Initial에서 시작되는 과정을 비교할 수 있다.

3. GA operator
>Pool을 생성하고 컨트롤하는 클래스이다.
>Pool이 사용하는 Evolution이나 Local Optimization의 방법을 지정할 수 있다.
>결과값을 정리해서 Visualization에 넘겨준다.

4. Visualization
>Data Generator에서 생성한 데이터, GA operator에서 계산한 solution을 이차원 그래프에 나타낸다.

5. Data Generator
>정류장 데이터(정류장 위치, 정류장 사이의 거리 등)와 수요 데이터(언제 어디에서 타고, 언제 어디에서 내리는지)를 랜덤하게 생성한다.
>그리고 GA operator에게 넘겨줘서 최적의 solution을 도출하게 한다.
