# ttsfront
frontend for realtime TTS using AI. (specifically coqui + realtimetts)

Sorry for such a complex install but python is stupid. I had no other choice ;-;.
I'll try to make this easier as i update it over time (there are other things i want to add too)

Installation:

1. Install python3.11.9 https://www.python.org/downloads/release/python-3119/
2. (on windows) Install C++ Visual Studio Build Tools https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. For nvidia-gpu support (recommended(especially on windows)) get 
https://developer.nvidia.com/cuda-11-8-0-download-archive and 
https://developer.nvidia.com/rdp/cudnn-archive.
3. Install ffmpeg. (on windows) Install Chocolatey. https://chocolatey.org/install#individual
4. Download ttsfront from https://github.com/tznl/ttsfront/archive/refs/heads/main.zip
5. Run scripts/install.bat for windows. Run install.sh for Linux.
6. Extract the contents of voice.zip into voice/. https://drive.google.com/file/d/1q1xOcSnVfA-Bk3jRyA7KcLVn365ibBk0/view?usp=sharing

Only for Windows.

1. Install Virtual Audio Cable https://vb-audio.com/Cable/
2. On reboot go to sound settings (System > Sound)
3. Under "Choose your input device" select "CABLE Output"
4. Open ttsfront.
5. (System > Sound > App volume and device preferences) Specify ttsfront's input and output and the designated "CABLE" input and output.
6. Whenever you want to use this program as a microphone make sure to select "CABLE" as the microphone name.
7. Run scripts/update.bat when needed.

Run this by executing/clicking main.py
