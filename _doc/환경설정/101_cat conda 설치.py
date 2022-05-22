cat requirements.txt | xargs -n 1 conda install

Macbook m1에서 xgboost 코드 실행시 segmentation fault 해결 - 멈춤보단 천천히라도​
    https://webnautes.tistory.com/1654    
​
https://pareekshithkatti.medium.com/setting-up-python-for-data-science-on-m1-mac-ced8a0d05911

1. pycaret를 설치합니다.
​
pip install --no-dependencies pycaret
​
2. 다음 목록을 pycaret_requirements.txt 파일 이름으로 저장후 다음 명령으로 설치를 진행합니다.
​
cat pycaret_requirements.txt | xargs -n 1 conda install

