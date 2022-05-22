Windows 11의 WSL2에서 GPU를 인식하고 PyTorch 사용



Windows 11 WSL2 GPU 

https://intrepidgeeks.com/tutorial/gpu-aware-and-pytorch-enabled-in-wsl2-on-windows-11

https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl
https://docs.nvidia.com/cuda/wsl-user-guide/index.html

WSL2-초간단-설치-및-CUDAGPU-설정-방법
    https://velog.io/@jaehyeong/WSL2-%EC%B4%88%EA%B0%84%EB%8B%A8-%EC%84%A4%EC%B9%98-%EB%B0%8F-CUDAGPU-%EC%84%A4%EC%A0%95-%EB%B0%A9%EB%B2%95


https://0verc10ck.tistory.com/43

Windows 11 upgrade


# To activate this environment, use
#
#     $ conda activate py38_cr
#
# To deactivate an active environment, use
#
#     $ conda deactivate

conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch

conda uninstall pytorch torchvision torchaudio 

4. PyTorch에서 GPU 동작 확인

Ubuntu에서 다음과 같이 Python을 실행합니다. CUDA 11.3 Ubuntu에 있는 PyTorch로 되돌아오면 GPU를 사용할 수 있습니다!
$ python
>>> import torch
>>> print(torch.cuda.is_available())
True
