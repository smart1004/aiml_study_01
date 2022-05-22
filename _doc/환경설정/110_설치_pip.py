
https://webnautes.tistory.com/1654
https://pareekshithkatti.medium.com/setting-up-python-for-data-science-on-m1-mac-ced8a0d05911
https://keepdev.tistory.com/27



conda list 저장하기(export 하기)
conda list --export > conda_packages.txt

#환경 만들기 
conda create -n py38_conda python=3.8
"""        
    conda create --name py38_conda1 --file conda_packages.txt python=3.8    
"""


1. pycaret를 설치합니다.
pip install --no-dependencies pycaret==2.3.10
pip install cufflinks==0.17.3 boruta==0.3 colorlover==0.3.0
    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    pycaret 2.3.10 requires gensim<4.0.0, which is not installed.
    pycaret 2.3.10 requires imbalanced-learn==0.7.0, which is not installed.
    pycaret 2.3.10 requires kmodes>=0.10.1, which is not installed.
    pycaret 2.3.10 requires lightgbm>=2.3.1, which is not installed.
    pycaret 2.3.10 requires matplotlib, which is not installed.
    pycaret 2.3.10 requires mlflow, which is not installed.
    pycaret 2.3.10 requires mlxtend>=0.17.0, which is not installed.
    pycaret 2.3.10 requires nltk, which is not installed.
    pycaret 2.3.10 requires numba<0.55, which is not installed.
    pycaret 2.3.10 requires pandas-profiling>=2.8.0, which is not installed.
    pycaret 2.3.10 requires pyLDAvis, which is not installed.
    pycaret 2.3.10 requires pyod, which is not installed.
    pycaret 2.3.10 requires pyyaml<6.0.0, which is not installed.
    pycaret 2.3.10 requires scikit-plot, which is not installed.
    pycaret 2.3.10 requires seaborn, which is not installed.
    pycaret 2.3.10 requires spacy<2.4.0, which is not installed.
    pycaret 2.3.10 requires textblob, which is not installed.
    pycaret 2.3.10 requires umap-learn, which is not installed.
    pycaret 2.3.10 requires wordcloud, which is not installed.
    pycaret 2.3.10 requires yellowbrick>=1.0.1, which is not installed.
    pycaret 2.3.10 requires scikit-learn==0.23.2, but you have scikit-learn 1.1.1 which is incompatible.
    pycaret 2.3.10 requires scipy<=1.5.4, but you have scipy 1.8.1 which is incompatible.
    
    
    ($ conda create --name py38_conda1 --file conda_packages.txt python=3.8
        Solving environment: failed
        PackagesNotFoundError: The following packages are not available from current channels:
          - pycaret==2.3.10=pypi_0
          - cufflinks==0.17.3=pypi_0
          - boruta==0.3=pypi_0
          - colorlover==0.3.0=pypi_0


* conda list 불러오기(Import 하기, 새로운 가상환경에서 다시 install 하기)
conda install --file conda_packages.txt


python -m ipykernel install --user --name py38_conda1 --display-name "py38_conda1"


conda install shap

conda install shap openpyxl
conda install -c conda-forge shap openpyxl
 
pip install openpyxl==3.0.9 shap==0.40.0

conda activate py38_conda1

