wsl vscode conda

(py38_cr5) kusung@DESKTOP-0DNI57Q:~/mylab/aiml_study_01$ which python
/home/kusung/miniconda3/envs/py38_cr5/bin/python


2. PATH에 추가하기
일반적으로 자동으로 경로에 추가되지 않기 때문에 아래와 같은 방법으로 anaconda bin 폴더를 경로에 추가해 주어야 합니다. 이를 위해서 WSL의 ~/.bashrc가장 밑에 아래의 명령어를 추가해 주어야 합니다.

export PATH=/home/ghkim/anaconda3/bin:$PATH
이때, 주의할 점은 위의 추가한 경로에 /home 뒤에 ghkim을 본인의 WSL 계정 명 으로 설정해 주어야 한다는 것 입니다.

export PATH=/home/kusung/miniconda3/envs/py38_cr5/bin:$PATH

cd /home/kusung/mylab
conda activate py38_cr5
code .

2. VSCode insider에서 인터프리터 설정해주기
이 부분은 이전에 VSCode insider와 WSL python interpreter를 연결할 때 python2를 3으로 바꾼 과정과 정확히 동일합니다. ctrl + shift + p 를 누른 뒤, select interpreter를 검색하고, 아래 그림과 같이 anaconda interpreter를 선택해주면 됩니다. 만약 anaconda interpreter가 보이지 않는다면, VSCode insider와 WSL을 각각 종료했다가 다시 실행하면 해결 될 것 입니다.

\\wsl.localhost\Ubuntu-20.04\home\kusung\.jupyter\jupyter_notebook_config.py
c.NotebookApp.notebook_dir = '/home/kusung/mylab'
c.NotebookApp.open_browser = False


