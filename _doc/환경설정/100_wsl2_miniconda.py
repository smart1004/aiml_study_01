To activate this environment, use
conda activate py38_cr3
jupyter lab --no-browser

Configuring Jupyter Notebook in Windows Subsystem Linux (WSL2)

https://towardsdatascience.com/configuring-jupyter-notebook-in-windows-subsystem-linux-wsl2-c757893e9d69
# 설치된 wsl 목록 확인
PS C:\Users\admin> wslconfig.exe /l
Linux 배포용 Windows 하위 시스템:
Ubuntu-20.04(기본값)

# 설치된 wsl 목록 삭제
PS C:\Users\admin> wslconfig.exe /u Ubuntu-20.04
삭제중...

# 이후 확인하면 설치된 wsl목록이 없음
PS C:\Users\admin> wslconfig.exe /l
Windows Subsystem for Linux has no installed distributions.
Distributions can be installed by visiting the Windows Store:
https://aka.ms/wslstore

# 이후 Ubuntu 디렉토리 삭제 진행

wsl --install -d Ubuntu-20.04

kusung/sinbal9!



cd ~
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh


Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[no] >>> yes
no change     /home/kusung/miniconda3/condabin/conda
no change     /home/kusung/miniconda3/bin/conda
no change     /home/kusung/miniconda3/bin/conda-env
no change     /home/kusung/miniconda3/bin/activate
no change     /home/kusung/miniconda3/bin/deactivate
no change     /home/kusung/miniconda3/etc/profile.d/conda.sh
no change     /home/kusung/miniconda3/etc/fish/conf.d/conda.fish
no change     /home/kusung/miniconda3/shell/condabin/Conda.psm1
no change     /home/kusung/miniconda3/shell/condabin/conda-hook.ps1
no change     /home/kusung/miniconda3/lib/python3.9/site-packages/xontrib/conda.xsh
no change     /home/kusung/miniconda3/etc/profile.d/conda.csh
modified      /home/kusung/.bashrc

==> For changes to take effect, close and re-open your current shell. <==

If you'd prefer that conda's base environment not be activated on startup,
   set the auto_activate_base parameter to false:

conda config --set auto_activate_base false

Thank you for installing Miniconda3!
kusung@DESKTOP-0DNI57Q:~$



pycaret Python 3.8 for Ubuntu


#환경 만들기
conda create -n py38_cr5 python=3.8

# To activate this environment, use
#     $ conda activate py38_cr5

# To deactivate an active environment, use
#
#     $ conda deactivate

#conda install pycaret=2.3.5

conda config --add channels conda-forge

$ pip install --upgrade pip
$ conda update -n base conda
$ conda update --all


pip install pycaret==2.3.5
#conda install -c conda-forge pycaret=2.3.5

    Successfully installed Boruta-0.3 Flask-2.1.2 IPython-8.3.0 Mako-1.2.0 PyWavelets-1.3.0 PyYAML-6.0 Send2Trash-1.8.0 Werkzeug-2.1.2 alembic-1.7.7 argon2-cffi-21.3.0 argon2-cffi-bindings-21.2.0 asttokens-2.0.5 attrs-21.4.0 backcall-0.2.0 beautifulsoup4-4.11.1 bleach-5.0.0 blis-0.7.7 catalogue-1.0.0 certifi-2022.5.18.1 cffi-1.15.0 charset-normalizer-2.0.12 click-8.1.3 cloudpickle-2.1.0 colorlover-0.3.0 cufflinks-0.17.3 cycler-0.11.0 cymem-2.0.6 databricks-cli-0.16.6 debugpy-1.6.0 decorator-5.1.1 defusedxml-0.7.1 docker-5.0.3 entrypoints-0.4 executing-0.8.3 fastjsonschema-2.15.3 fonttools-4.33.3 funcy-1.17 future-0.18.2 gensim-3.8.3 gitdb-4.0.9 gitpython-3.1.27 greenlet-1.1.2 gunicorn-20.1.0 htmlmin-0.1.12 idna-3.3 imagehash-4.2.1 imbalanced-learn-0.7.0 importlib-metadata-4.11.3 importlib-resources-5.7.1 ipykernel-6.13.0 ipython-genutils-0.2.0 ipywidgets-7.7.0 itsdangerous-2.1.2 jedi-0.18.1 jinja2-3.1.2 joblib-1.1.0 jsonschema-4.5.1 jupyter-client-7.3.1 jupyter-core-4.10.0 jupyterlab-pygments-0.2.2 jupyterlab-widgets-1.1.0 kiwisolver-1.4.2 kmodes-0.12.1 lightgbm-3.3.2 llvmlite-0.38.1 markupsafe-2.1.1 matplotlib-3.5.2 matplotlib-inline-0.1.3 missingno-0.5.1 mistune-0.8.4 mlflow-1.26.0 mlxtend-0.19.0 multimethod-1.8 murmurhash-1.0.7 nbclient-0.6.3 nbconvert-6.5.0 nbformat-5.4.0 nest-asyncio-1.5.5 networkx-2.8.1 nltk-3.7 notebook-6.4.11 numba-0.55.1 numexpr-2.8.1 numpy-1.19.5 oauthlib-3.2.0 packaging-21.3 pandas-1.4.2 pandas-profiling-3.2.0 pandocfilters-1.5.0 parso-0.8.3 patsy-0.5.2 pexpect-4.8.0 phik-0.12.2 pickleshare-0.7.5 pillow-9.1.1 plac-1.1.3 plotly-5.8.0 preshed-3.0.6 prometheus-client-0.14.1 prometheus-flask-exporter-0.20.1 prompt-toolkit-3.0.29 protobuf-3.20.1 psutil-5.9.1 ptyprocess-0.7.0 pure-eval-0.2.2 pyLDAvis-3.2.2 pycaret-2.3.5 pycparser-2.21 pydantic-1.9.1 pygments-2.12.0 pyjwt-2.4.0 pynndescent-0.5.7 pyod-1.0.1 pyparsing-3.0.9 pyrsistent-0.18.1 python-dateutil-2.8.2 pytz-2022.1 pyzmq-23.0.0 querystring-parser-1.2.4 regex-2022.4.24 requests-2.27.1 scikit-learn-0.23.2 scikit-plot-0.3.7 scipy-1.5.4 seaborn-0.11.2 six-1.16.0 smart-open-6.0.0 smmap-5.0.0 soupsieve-2.3.2.post1 spacy-2.3.7 sqlalchemy-1.4.36 sqlparse-0.4.2 srsly-1.0.5 stack-data-0.2.0 statsmodels-0.13.2 tabulate-0.8.9 tangled-up-in-unicode-0.2.0 tenacity-8.0.1 terminado-0.15.0 textblob-0.17.1 thinc-7.4.5 threadpoolctl-3.1.0 tinycss2-1.1.1 tornado-6.1 tqdm-4.64.0 traitlets-5.2.1.post0 typing-extensions-4.2.0 umap-learn-0.5.3 urllib3-1.26.9 visions-0.7.4 wasabi-0.9.1 wcwidth-0.2.5 webencodings-0.5.1 websocket-client-1.3.2 widgetsnbextension-3.6.0 wordcloud-1.8.1 yellowbrick-1.3.post1 zipp-3.8.0



pycaret-2.3.10
	Successfully installed Boruta-0.3 Flask-2.1.2 IPython-8.3.0 Mako-1.2.0 PyWavelets-1.3.0 Send2Trash-1.8.0 Werkzeug-2.1.2 alembic-1.7.7 argon2-cffi-21.3.0 argon2-cffi-bindings-21.2.0 asttokens-2.0.5 attrs-21.4.0 backcall-0.2.0 beautifulsoup4-4.11.1 bleach-5.0.0 blis-0.7.7 catalogue-1.0.0 certifi-2022.5.18.1 cffi-1.15.0 charset-normalizer-2.0.12 click-8.1.3 cloudpickle-2.1.0 colorlover-0.3.0 cufflinks-0.17.3 cycler-0.11.0 cymem-2.0.6 databricks-cli-0.16.6 debugpy-1.6.0 decorator-5.1.1 defusedxml-0.7.1 docker-5.0.3 entrypoints-0.4 executing-0.8.3 fastjsonschema-2.15.3 fonttools-4.33.3 funcy-1.17 future-0.18.2 gensim-3.8.3 gitdb-4.0.9 gitpython-3.1.27 greenlet-1.1.2 gunicorn-20.1.0 htmlmin-0.1.12 idna-3.3 imagehash-4.2.1 imbalanced-learn-0.7.0 importlib-metadata-4.11.3 importlib-resources-5.7.1 ipykernel-6.13.0 ipython-genutils-0.2.0 ipywidgets-7.7.0 itsdangerous-2.1.2 jedi-0.18.1 jinja2-3.1.2 joblib-1.1.0 jsonschema-4.5.1 jupyter-client-7.3.1 jupyter-core-4.10.0 jupyterlab-pygments-0.2.2 jupyterlab-widgets-1.1.0 kiwisolver-1.4.2 kmodes-0.12.1 lightgbm-3.3.2 llvmlite-0.37.0 markupsafe-2.1.1 matplotlib-3.5.2 matplotlib-inline-0.1.3 missingno-0.5.1 mistune-0.8.4 mlflow-1.26.0 mlxtend-0.19.0 multimethod-1.8 murmurhash-1.0.7 nbclient-0.6.3 nbconvert-6.5.0 nbformat-5.4.0 nest-asyncio-1.5.5 networkx-2.8.1 nltk-3.7 notebook-6.4.11 numba-0.54.1 numexpr-2.8.1 numpy-1.19.5 oauthlib-3.2.0 packaging-21.3 pandas-1.4.2 pandas-profiling-3.2.0 pandocfilters-1.5.0 parso-0.8.3 patsy-0.5.2 pexpect-4.8.0 phik-0.12.2 pickleshare-0.7.5 pillow-9.1.1 plac-1.1.3 plotly-5.8.0 preshed-3.0.6 prometheus-client-0.14.1 prometheus-flask-exporter-0.20.1 prompt-toolkit-3.0.29 protobuf-3.20.1 psutil-5.9.1 ptyprocess-0.7.0 pure-eval-0.2.2 pyLDAvis-3.2.2 pycaret-2.3.10 pycparser-2.21 pydantic-1.9.1 pygments-2.12.0 pyjwt-2.4.0 pynndescent-0.5.7 pyod-1.0.1 pyparsing-3.0.9 pyrsistent-0.18.1 python-dateutil-2.8.2 pytz-2022.1 pyyaml-5.4.1 pyzmq-23.0.0 querystring-parser-1.2.4 regex-2022.4.24 requests-2.27.1 scikit-learn-0.23.2 scikit-plot-0.3.7 scipy-1.5.4 seaborn-0.11.2 six-1.16.0 smart-open-6.0.0 smmap-5.0.0 soupsieve-2.3.2.post1 spacy-2.3.7 sqlalchemy-1.4.36 sqlparse-0.4.2 srsly-1.0.5 stack-data-0.2.0 statsmodels-0.13.2 tabulate-0.8.9 tangled-up-in-unicode-0.2.0 tenacity-8.0.1 terminado-0.15.0 textblob-0.17.1 thinc-7.4.5 threadpoolctl-3.1.0 tinycss2-1.1.1 tornado-6.1 tqdm-4.64.0 traitlets-5.2.1.post0 typing-extensions-4.2.0 umap-learn-0.5.3 urllib3-1.26.9 visions-0.7.4 wasabi-0.9.1 wcwidth-0.2.5 webencodings-0.5.1 websocket-client-1.3.2 widgetsnbextension-3.6.0 wordcloud-1.8.1 yellowbrick-1.3.post1 zipp-3.8.0


Anaconda Prompt를 열어서 진행합니다.


conda config --set channel_priority false

jupyterlab pycaret



conda install -c conda-forge jupyterlab
    conda install -c conda-forge jupyterlab jupyter_contrib_nbextensions
    conda install -c conda-forge cudatoolkit=11.3
        Collecting package metadata (current_repodata.json): done
        Solving environment: done
        ## Package Plan ##
        environment location: /home/kusung/miniconda3/envs/py38_cr2
        The following NEW packages will be INSTALLED:
          cudatoolkit        pkgs/main/linux-64::cudatoolkit-11.3.1-h2bc3f7f_2

    conda install pip git








# envs 위치
/home/kusung/miniconda3/envs/py38_cr2



1. Jupyter Notebook 환경 설정 파일 생성
    ① 명령창 (Command 실행 또는 Anaconda 사용중인 경우 Anaconda Prompt 실행)
    ② 명령창에 아래 명령
    jupyter notebook --generate-config
    경로   
    (py38_cr) kusung@DESKTOP-0DNI57Q:~$ jupyter notebook --generate-config
    Writing default config to: /home/kusung/.jupyter/jupyter_notebook_config.py
    (py38_cr) kusung@DESKTOP-0DNI57Q:~$
    vim /home/kusung/.jupyter/jupyter_notebook_config.py
 

    # notebook_dir
    # c.NotebookApp.notebook_dir = ''
    c.NotebookApp.notebook_dir = '/mnt/d/mylab'
    c.NotebookApp.notebook_dir = 'D:\mylab'

    윈도우 폴더와 공유를 하고 싶다.
        
    D:\mylab\
        cd /mnt/d/mylab
        
WSL 폴더를 윈도우와 함께 사용하기
    https://itun.tistory.com/637    
    \\wsl$\Ubuntu-20.04
    
    
https://towardsdatascience.com/configuring-jupyter-notebook-in-windows-subsystem-linux-wsl2-c757893e9d69
    
    
    


"""
    importError: Numba needs NumPy 1.21 or less    
    NumPy 1.21 
    conda install -c conda-forge NumPy==1.21  

    pip install Pillow==9.1.1
    pillow-9.1.1

    pip install --upgrade --force-reinstall Pillow
    pip install --upgrade --force-reinstall matplotlib==3.5.2

    matplotlib-3.5.2

    pip install --upgrade --force-reinstall numpy==1.19.5

"""


pip uninntall pycaret    

pip install pycaret==2.3.5
pip install jupyter_contrib_nbextensions


python -m ipykernel install --user --name py38_cr5 --display-name "py38_cr5"
Installed kernelspec py38_cr in /home/kusung/.local/share/jupyter/kernels/py38_cr2

jupyter kernelspec list

jupyter kernelspec uninstall 가상환경이름
jupyter kernelspec uninstall py38_cr5

install pycaret jupyter lab


http://localhost:8888/lab?token=4177e2b2c9dbac076a4c1b42d16d80c241676c7e3f50eb8b





rm -rf py38_cr2
    # rm 명령어를 사용하는 삭제 방법
    rm을 사용할 경우 아래와 같이 옵션을 설정할 수 있습니다.
    r : 파일 디렉토리 함께 삭제하기
    f : 파일 유무와 상관없이 삭제하기


# \\wsl.localhost\Ubuntu-20.04\home\kusung\.jupyter\jupyter_notebook_config.py
c.NotebookApp.notebook_dir = '/mnt/d/mylab'
c.NotebookApp.open_browser = False

