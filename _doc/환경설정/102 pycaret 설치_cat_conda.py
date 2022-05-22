rm -rf py38_cr2

https://webnautes.tistory.com/1654
https://pareekshithkatti.medium.com/setting-up-python-for-data-science-on-m1-mac-ced8a0d05911

#환경 만들기
conda create -n py38_cr_pip python=3.8

# To activate this environment, use
#     $ conda activate py38_cr2

# To deactivate an active environment, use
#
#     $ conda deactivate

#conda install pycaret=2.3.5

1. pycaret를 설치합니다.
pip install --no-dependencies pycaret

2. 다음 목록을 pycaret_requirements.txt 파일 이름으로 저장후 다음 명령으로 설치를 진행합니다.

cat pycaret_requirements.txt | xargs -n 1 conda install

pandas
scipy
numpy
seaborn
matplotlib
IPython
joblib
scikit-learn
ipywidgets
yellowbrick>=1.0.1
lightgbm>=2.3.1
plotly>=4.4.1
wordcloud
textblob
cufflinks>=0.17.0
umap-learn
pyLDAvis
gensim
spacy
nltk
mlxtend>=0.17.0
pyod
pandas-profiling>=2.8.0
kmodes>=0.10.1
mlflow
imbalanced-learn
scikit-plot  
Boruta
numba
 
 
설치하려는 라이브러리가 많은 경우 이를 require.txt 파일에 넣고 사용할 수 있습니다.

cat requirements.txt | xargs -n 1 conda install

이렇게 하면 단일 라이브러리로 인해 conda가 실패하는 것을 방지할 수 있습니다.

그런 다음 conda에서 설치하지 않은 라이브러리를 pip install로 시도할 수 있습니다.

다음을 사용하여 이러한 라이브러리를 알 수 있습니다.

conda install --file requirements.txt


설치되지 않은 모든 패키지에 대해 pip 설치했습니다.

pip install cufflinks boruta


pip install cufflinks boruta 

ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
pycaret 2.3.10 requires gensim<4.0.0, but you have gensim 4.1.2 which is incompatible.
pycaret 2.3.10 requires imbalanced-learn==0.7.0, but you have imbalanced-learn 0.9.1 which is incompatible.
pycaret 2.3.10 requires numba<0.55, but you have numba 0.55.1 which is incompatible.
pycaret 2.3.10 requires pyyaml<6.0.0, but you have pyyaml 6.0 which is incompatible.
pycaret 2.3.10 requires scikit-learn==0.23.2, but you have scikit-learn 1.1.1 which is incompatible.
pycaret 2.3.10 requires scipy<=1.5.4, but you have scipy 1.8.1 which is incompatible.
pycaret 2.3.10 requires spacy<2.4.0, but you have spacy 3.3.0 which is incompatible.


gensim<4.0.0
imbalanced-learn==0.7.0
numba<0.55
pyyaml<6.0.0
scikit-learn==0.23.2
scipy<=1.5.4
scipy<=1.5.4
spacy<2.4.0

cat pycaret_requirements2.txt | xargs -n 1 conda install





conda install jupyterlab
