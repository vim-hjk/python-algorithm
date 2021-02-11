import matplotlib.pyplot as plt
from sympy import *

# 데이터 선언
X = [1, 2, 3, 4]
Y = [5, 7, 9, 11]

# 변수 명시화
W, b, x, y = symbols('w, b, x, y')

# 수식 정의
Hypothesis = W * x + b
descent_W_polynomial = diff(expand((Hypothesis - y)**2), W)     # 가중치에 대하여 편미분
descent_b_polynomial = diff(expand((Hypothesis - y)**2), b)     # 편향에 대하여 편미분
cost_polynomial = (Hypothesis - y)**2       # 최소 제곱법 수식

# 가중치와 편향 초기화
weight = 1
bias = 0

# 학습률 설정
learning_rate = 0.01

# 변수 초기화
sum_cost = 0
sum_desenct_W = 0
sum_desenct_b = 0


# 다항식의 변수에 값을 대입하여 계산하는 함수
def Calculate_polynomial(me, weight, X, bias, Y):
    result = me.subs([(W, weight), (x, X), (b, bias), (y, Y)])
    return result


# 2000번 학습
for step in range(2001):
    for i in range(len(X)):
        sum_cost = sum_cost + Calculate_polynomial(cost_polynomial, weight, X[i], bias, Y[i])
        sum_desenct_W = sum_desenct_W + Calculate_polynomial(descent_W_polynomial, weight, X[i], bias, Y[i])        # 가중치에 대한 기울기 계산
        sum_desenct_b = sum_desenct_b + Calculate_polynomial(descent_b_polynomial, weight, X[i], bias, Y[i])        # 편향에 대한 기울기 계산
    cost = sum_cost / len(X)        # 비용 계산
    descent_W = sum_desenct_W / len(X)
    descent_b = sum_desenct_b / len(X)
    weight = weight - (learning_rate * descent_W)   # 가중치 갱신
    bias = bias - (learning_rate * descent_b)       # 편향 갱신
    # 변수 초기화
    sum_cost = 0
    sum_desenct_W = 0
    sum_desenct_b = 0
    # 100번 학습 시 마다 값 출력
    if step % 100 == 0:
        print("Epoch : {0}, Cost : {1}, W : {2:.4f}, b : {3:.4f}".format(step, float(cost), float(weight), float(bias)))


plt.scatter(X, Y)
plt.plot([x for x in range(len(X) + 1)], [weight * x + bias for x in range(len(X) + 1)], color="red")
plt.axis([-0.5, max(X) + 0.5, -0.5, max(Y) + 0.5])
plt.xlabel('X')
plt.ylabel('Y')
plt.show()