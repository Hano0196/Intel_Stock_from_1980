import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

def Benford_distribution(): # 벤포드의 법칙 비율 식을 이용해서 함수 생성
    return [np.log10((x + 1) / x) for x in range(1, 10)]

data = np.load("Intel_Stock_History_from_1980_03_17.npy") # 인텔 주가 데이터 로드
temp = [str(x) for x in data] # 데이터를 다듬는 과정
result = [int(x[0]) for x in temp] # 데이터를 다듬는 과정2
hist_result = np.histogram(result, bins=np.arange(1,11))[0] # 히스토그램 함수를 이용하여 구간을 나누고 (bins) 데이터 개수를 세어 분포를 나타냄
histogram = hist_result / sum(hist_result) # 막대 그래프를 그리기 위한 최종 데이터
benford = Benford_distribution() # 벤포드 법칙

xrange = range(1, 10) # x축의 범위는 1부터 9까지
plt.plot(xrange, np.array(benford) * 100, c='red', ls='--', marker='o') # 벤포드의 비율을 빨간 선형 그래프로 나타냄
plt.bar(xrange, histogram * 100) # 막대 그래프 (히스토그램)
plt.xlabel('Digit') # x축 라벨 추가
plt.ylabel('Percentage') # y축 라벨 추가
plt.xticks(xrange) # x축 범위
plt.title('Intel_Stock_from_1980') # 제목
plt.show() # 그래프 보여주기

chisq_test = chisquare(histogram, f_exp=benford) #카이제곱 검정
print(chisq_test)