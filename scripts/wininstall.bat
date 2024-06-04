git pull
python.exe -m pip install --upgrade pip
pip install RealtimeTTS
pip install torch==2.3.0+cu118 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
choco install ffmpeg
pip install openai keyboard realtimestt sounddevice readline
python -m venv ..\env_realtimetts
..\env_realtimetts\Scripts\activate.bat
echo:
echo:
echo:
echo:
echo:
echo "install script finished"
@pause
