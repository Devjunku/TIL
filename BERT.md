## BERT (Bidirectional Encoder representations from Transformer)

[https://www.youtube.com/watch?v=30SvdoA6ApE](https://www.youtube.com/watch?v=30SvdoA6ApE)

Bidirectional: 양방향

Encoder: 입력값을 숫자값으로 바꿈

문맥을 양방향으로 이해해서 숫자의 형태로 바꾸는 딥러닝 모델임

Transformer는 2017년에 구글에서 발표한 encoder + decoder 구조를 지닌 deeplearning 모델임. 아래와 같음

![스크린샷 2021-09-07 오전 10.15.15](python/img/스크린샷 2021-09-07 오전 10.15.15.png)

BERT가 나온데는 GPT라는 모형이 원인이 되었음

GPT(generative pre-training)

- **Transformer의 디코더를 적층**한 모델
- 디코더를 활용하여, 생성 모델에 적합
- Transformer를 활용한 pre-trained model의 시초



BERT의 경우 입력값은 인코더(숫자로 변환) 됨 이때 인코더는 Attention Vector를 생성함

Attention Vector는 토큰의 의미 구하기 위해서 사용됨. Attention Vector가 왜 있느냐?

예를 들어서 어떤 문서에 message와 text라는 단어가 존재한다고 하자.

만약에 text라는 단어만 존재한다면, 이 text가 신문속 text를 의미하는지 아니면 message를 의미하는지 모른다.

message만 존재한다고 해도 같은 반대로 같은 의미가 된다. 하지만 만약에 둘 다 존재한다면, 이 둘 단어가 의미하는 것은 특정 무언가를 가르킬 것이다.

따라서 이를 Attention Vector로 전달한다는 의미이다. 