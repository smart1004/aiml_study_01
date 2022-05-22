conda activate py38_cr5
jupyter lab --no-browser

jupyter kernelspec list

jupyter kernelspec uninstall 가상환경이름

​#create notebook kernel connected with the conda environment

python -m ipykernel install --user --name lab_05 --display-name "lab_05"

jupyter kernelspec --help
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
    
miniconda 환경 지우기
    cd /home/kusung/miniconda3/envs
    rm -rf py38_cr4

 