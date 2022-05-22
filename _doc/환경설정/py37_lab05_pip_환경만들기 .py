 D:\tools5\env_py37\py37_lab05_pip_환경만들기4_pycaret.py

​

바로가기 만들기

%windir%\System32\cmd.exe "/K" D:\tools5\env_py37\lab_05\Scripts\activate.bat &cd D:\tools5\env_py37\lab_05_manage\

​

​https://www.python.org/downloads/release/python-379/
https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe
==========

​

pip install virtualenv

​

>> which python

/c/tools/Python/Python37/python

c:/tools/Python/Python37/python

​

>> python.exe -m pip install --upgrade pip

>> C:\tools\Python\Python37\Scripts\pip install virtualenv

Installing collected packages: distlib, zipp, typing-extensions, six, platformdirs, filelock, importlib-metadata, virtualenv
  WARNING: The script virtualenv.exe is installed in 'c:\tools\python\python37\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed distlib-0.3.4 filelock-3.7.0 importlib-metadata-4.11.3 platformdirs-2.5.2 six-1.16.0 typing-extensions-4.2.0 virtualenv-20.14.1 zipp-3.8.0


# 새로운 버전의 파이썬 설치 시에만 하면 된다. ---->

#------------------------------

​

​

# 환경만들기 

# 생성폴더 :: D:\tools5\env_py37\lab_05\

cd D:\tools5\env_py37

# virtualenv \path\to\env -p path\to\new_python.exe

$ C:\tools\Python\Python37\Scripts\virtualenv lab_05 -p C:\tools\Python\Python37\python.exe

    C:\tools\Python\Python37>C:\tools\Python\Python37\Scripts\virtualenv lab_05 -p C:\tools\Python\Python37\python.exe
    created virtual environment CPython3.7.9.final.0-64 in 2346ms
      creator CPython3Windows(dest=C:\tools\Python\Python37\lab_05, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\kusung\AppData\Local\pypa\virtualenv)
        added seed packages: pip==22.0.4, setuptools==62.1.0, wheel==0.37.1
      activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
​

# activate

D:\tools5\env_py37\lab_05\Scripts\activate.bat



## 통상적인 패키지 관리

mkdir D:\tools5\env_py37\lab_05_manage

cd D:\tools5\env_py37\lab_05_manage

​

D:\tools5\env_py37\lab_05\Scripts\python.exe -m pip install --upgrade pip

​

​

​

""" 심플 버전에서는 아래는 설치하지 않는게 좋다. 패키지관리에 시간이 많이 소모된다.

poetry add pycaret=2.2.2 #얘는 왠만한 머신러닝 애들을 통합해 가지고 있다.

​poetry add tensorflow=2.1.0

"""

​

#poetry add pycaret=2.3.5

pip install pycaret==2.3.5

pip uninstall pycaret

​
pip install openpyxl==3.0.9 shap==0.40.0 jupyterlab
pip install openpyxl shap jupyterlab

#pip install openpyxl #openpyxl-3.0.9
#pip install shap #shap-0.40.0

​

​
​

​

​

​

​

​

========================================================================

바로가기 만들기

%windir%\System32\cmd.exe "/K" D:\tools5\env_py37\lab_05\Scripts\activate.bat &cd D:\tools5\env_py37\lab_05_manage\

​

ConEmu

C:\Users\ME\ 아래에 복사한다. 

ConEmu의 기본시작위치가 C:\Users\ME\ 이다.

이 밑에 activate.bat를 복사해두고 실행하면 된다.

activate.bat 마지막줄에 다음 문장을 추가한다. 경로이동 문장을 치기 귀찮아서

cd D:\tools5\env_py37\lab_05_manage\

​

​

jupyter kernelspec list

jupyter kernelspec uninstall 가상환경이름

​#create notebook kernel connected with the conda environment

python -m ipykernel install --user --name lab_05 --display-name "lab_05"

​
1. Jupyter Notebook 환경 설정 파일 생성
    ① 명령창 (Command 실행 또는 Anaconda 사용중인 경우 Anaconda Prompt 실행)
    ② 명령창에 아래 명령
    jupyter notebook --generate-config
    경로   
    (lab_05) D:\tools5\env_py37\lab_05_manage>jupyter notebook --generate-config
    Writing default config to: C:\Users\kusung\.jupyter\jupyter_notebook_config.py


    # notebook_dir
    # c.NotebookApp.notebook_dir = ''
    c.NotebookApp.notebook_dir = 'D:\mylab'

​

# poetry install

# poetry add mlprodict

​

​
​

​
기타 프로그램
CPU- Z는 CPU와 마더보드에 대한 일반적인 정보를 확인하는 데 있어 신뢰할 수 있는 도구입니다. 설치 후 실행하면 CPU와 마더보드의 정확한 모델 번호와 일부 성능 정보를 확인할 수 있습니다. 해당 모델 번호를 사용하여 CPU 사용량과 관련된 지원 스레드를 온라인으로 검색하십시오.

백그라운드 프로세스를 확인하는 방법이 작업 관리자만 있는 것은 아닙니다. Process Monitor는 CPU 사용량뿐 아니라 레지스트리, 파일 시스템, 네트워크 활동을 기록합니다. 이 도구를 사용하여 멀웨어로 의심되는 프로세스의 네트워크 활동을 확인합니다.

이와 유사한 성능 모니터는 시간 경과에 따른 프로세스의 CPU 사용량을 더 자세하게 확인할 수 있는 Windows 기본 탑재 도구입니다. 성능 모니터를 실행하려면 Windows 키와 R을 동시에 누르고 “perfmon”을 입력합니다.