"wsl2" python venv 3.7
pyenv wsl2

https://prod.velog.io/@ohdowon064/Python-install-pyenv-in-ubuntu

mkdir py37_env

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl  libncurses5-dev libncursesw5-dev \
xz-utils 

tk-dev llvm

Reading state information... Done
E: Unable to locate package llvm
E: Unable to locate package tk-dev



vim ~/.bashrc

# vi ~/.bashrc
export PYENV_ROOT="$HOME/.pyenv
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"


pyenv 사용하기
# python list 설치
pyenv install --list

# 원하는 python 버전 설치
pyenv install [파이썬버전]
pyenv install miniconda3-4.7.12

Install
PyCaret is tested and supported on the following 64-bit systems:
Python 3.6 – 3.8
Python 3.9 for Ubuntu only
Ubuntu 16.04 or later
Windows 7 or later


pyenv install 3.7.13
pyenv install 3.9.13

pyenv global 3.7.13
pyenv global miniconda3-4.7.12
# 설치된 파이썬 버전 확인
pyenv versions
"""
# 가상환경 만들기
pyenv virtualenvs [파이썬버전] [가상환경명]
pyenv virtualenvs 3.7.13 venv

# 가상환경 시작하기
pyenv activate [가상환경명]

# 가상환경 끝내기
pyenv deactivate

# 가상환경 목록 확인
pyenv virtualenvs

# 가상환경 삭제하기
pyenv uninstall [가상환경명]
"""

conda env 


https://docs.microsoft.com/ko-kr/windows/python/web-frameworks



sudo apt update && sudo apt upgrade

pip install pycaret==2.3.5



wsl2 pycaret

############################################### 
# 미니콘다-wsl2-vsc-파이썬
https://smoothiecoding.kr/%EB%AF%B8%EB%8B%88%EC%BD%98%EB%8B%A4-wsl2-vsc-%ED%8C%8C%EC%9D%B4%EC%8D%AC/

Installed Miniconda3-4.7.12-Linux-x86_64 to /home/kusung/.pyenv/versions/miniconda3-4.7.12


pycaret Python 3.8 for Ubuntu

conda create -n py38_cr python=3.8

conda install -c conda-forge pycaret==2.3.5
#
# To activate this environment, use
#
#     $ conda activate py38_cr
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(py38_cr) conda install -c conda-forge pycaret==2.3.5
Collecting package metadata (current_repodata.json): done
Solving environment: failed with initial frozen solve. Retrying with flexible solve.
Collecting package metadata (repodata.json): done
Solving environment: -

(py38_cr) pip install pycaret




Collecting pyLDAvis
  Downloading pyLDAvis-3.3.0.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 10.5 MB/s
  Installing build dependencies ... error
  ERROR: Command errored out with exit status 1:
   command: /home/kusung/.pyenv/versions/miniconda3-4.7.12/envs/py38_cr/bin/python /tmp/pip-standalone-pip-na0ajkr6/__env_pip__.zip/pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-vzg_8tk2/overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- setuptools
       cwd: None
  Complete output (7 lines):
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f20b9b96a60>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution')': /simple/setuptools/
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f20b9b96760>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution')': /simple/setuptools/
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f20b9b96640>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution')': /simple/setuptools/
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f20b9b96310>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution')': /simple/setuptools/
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.HTTPSConnection object at 0x7f20b9bb43a0>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution')': /simple/setuptools/
  ERROR: Could not find a version that satisfies the requirement setuptools (from versions: none)
  ERROR: No matching distribution found for setuptools
  ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/7a/f0/0bad54f2ebe51e0aa09c6f69f53204f499b97b35b4d969d2c6644f48d834/pyLDAvis-3.3.0.tar.gz#sha256=828677860409ebf11b6077a4589a30ab94f51dc4b2f8751105aae8d95dd28dd4 (from https://pypi.org/simple/pyldavis/). Command errored out with exit status 1: /home/kusung/.pyenv/versions/miniconda3-4.7.12/envs/py38_cr/bin/python /tmp/pip-standalone-pip-na0ajkr6/__env_pip__.zip/pip install --ignore-installed --no-user --prefix /tmp/pip-build-env-vzg_8tk2/overlay --no-warn-script-location --no-binary :none: --only-binary :none: -i https://pypi.org/simple -- setuptools Check the logs for full command output.
  Downloading pyLDAvis-3.2.2.tar.gz (1.7 MB)
     |████████████████████████████████| 1.7 MB 7.0 MB/s
Collecting future
  Downloading future-0.18.2.tar.gz (829 kB)
     |████████████████████████████████| 829 kB 4.2 MB/s
Collecting statsmodels
  Downloading statsmodels-0.13.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (9.9 MB)
  
  
  
Ubuntu 설정
    This message is shown once a day. To disable it please create the
    /home/kusung/.hushlogin file.  
  
  
  
  
To activate this environment, use
conda activate py38_cr
jupyter lab 

To deactivate an active environment, use
    conda deactivate


제어판\시스템 및 보안\Windows Defender 방화벽  막혀 있어니 뭔가 안된다.

 
Vmmem-점유율-해결하기
    https://velog.io/@xonic789/Vmmem-%EC%A0%90%EC%9C%A0%EC%9C%A8-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0

    파일 탐색기를 열어 %USERPROFILE%를 입력 후
    해당 경로에 .wslconfig 파일을 만든다.
    notepad로 연다.
    [wsl2]
    memory=8GB
    swap=0
    localhostForwarding=true
    를 입력 후 저장한다!
    4. 재부팅하면 바로 확인 가능!
    
    [wsl2]
    memory=16GB
    swap=0
    processors=7
    localhostForwarding=true
    
    
윈도우 cpu core 확인
    1. 실행 커맨드로 msinfo32 
    2. 시스템 정보 확인
       8 core 16 논리프로세스
    
wsl-customize-resource    
    https://seokbeomkim.github.io/posts/wsl-customize-resource/
    
    
shutdown    
    wsl -l -v
          NAME      STATE           VERSION
        * Ubuntu    Running         2
    wsl -t Ubuntu-20.04 --shutdown
    
    

    
    
    
    
jupyter kernelspec list

jupyter kernelspec uninstall 가상환경이름


​#create notebook kernel connected with the conda environment
python -m ipykernel install --user --name py38_cr --display-name "py38_cr"   


    (py38_cr) kusung@DESKTOP-0DNI57Q:/mnt/d$ jupyter kernelspec list
    Available kernels:
      python3    /home/kusung/.pyenv/versions/miniconda3-4.7.12/envs/py38_cr/share/jupyter/kernels/python3
    (py38_cr) kusung@DESKTOP-0DNI57Q:/mnt/d$ python -m ipykernel install --user --name py38_cr --display-name "py38_cr"
    Installed kernelspec py38_cr in /home/kusung/.local/share/jupyter/kernels/py38_cr
    (py38_cr) kusung@DESKTOP-0DNI57Q:/mnt/d$


1. Jupyter Notebook 환경 설정 파일 생성
    ① 명령창 (Command 실행 또는 Anaconda 사용중인 경우 Anaconda Prompt 실행)
    ② 명령창에 아래 명령
    jupyter notebook --generate-config
    경로   
    (py38_cr) kusung@DESKTOP-0DNI57Q:/mnt/d$ jupyter notebook --generate-config
    Writing default config to: /home/kusung/.jupyter/jupyter_notebook_config.py
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

아래는 적용하지 않다    
"""    
    https://codeac.tistory.com/118  


    WSL2 활용도를 높여주는 고정 IP 설정
        https://netmarble.engineering/wsl2-static-ip-scheduler-settings/
        
        
    WSL2 Ubuntu 20.04 및 네트워크 설정
        http://shaun289.blogspot.com/2020/06/wsl2-ubuntu-2004.html


    https://superroot.tistory.com/275
"""

ifconfig -a 
sudo apt install net-tools

 

0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 459 kB disk space will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 38476 files and directories currently installed.)
Removing libfwupdplugin1:amd64 (1.5.11-0ubuntu1~20.04.2) ...
Processing triggers for libc-bin (2.31-0ubuntu9.9) ...
/sbin/ldconfig.real: /usr/lib/wsl/lib/libcuda.so.1 is not a symbolic link

