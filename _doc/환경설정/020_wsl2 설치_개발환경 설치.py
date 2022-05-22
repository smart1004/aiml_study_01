1111
wsl2 설치

$ dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

$ dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --install -d Ubuntu

wsl --install -d Ubuntu-20.04

실행 중인 WSL 버전 확인
PowerShell 또는 Windows 명령 프롬프트에서 wsl -l -v 명령을 입력하여 설치된 Linux 배포판을 나열하고 각각 설정된 WSL 버전을 확인할 수 있습니다.
wsl -l -v

wsl --set-version Ubuntu-20.04 2


3. 설치된 wsl ubuntu 삭제하기

wslconfig.exe /u ubuntu