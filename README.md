# Intrusion-Detection-System
This is a system for detecting home intrusion .

## System Operations
Initially Images are captured using CCTV camera connected to the Raspberry pi, then the images from the Raspberry pi will be sent to an AWS Windows VM (capturing and sending images from linux to windows is done through a bash script). 
The VM itself has UiPath studio running with the necessary python ML models. Each image being captured will be sent to the VM running UiPath for movement and object detection. It is necessary to train the faces of the householders for the model to classify them as safe, additionally it can also identify animals and birds if the customer wishes, so there is no gap for false alerts. If an unregistered face is detected, it tries to take images of their face and sends an e-mail to the owner of the household for further confirmation. If the owner identifies them as an intruder, the bot provides options to contact emergency numbers or police directly and can inform about the incident.


## Hardware and Software requirements
### Hardware:
Rasperry pi<br />
cctv camera<br />

### Software:
### Base ----------------------------------------
matplotlib>=3.2.2,<br />
numpy>=1.18.5,<br />
opencv-python>=4.1.2,<br />
Pillow>=7.1.2,<br />
PyYAML>=5.3.1,<br />
requests>=2.23.0,<br />
scipy>=1.4.1,<br />
torch>=1.7.0,<br />
torchvision>=0.8.1,<br />
tqdm>=4.41.0,<br />

### Logging -------------------------------------
tensorboard>=2.4.1,<br />

### Plotting ------------------------------------
pandas>=1.1.4,<br />
seaborn>=0.11.0,<br />

### Face-recognition ----------------------------
dlib,<br />
face_recognition,<br />
cmake for face-recognition download the .msi file and install with path set. Use this link to download https://cmake.org/download/,<br />

### Raspberry pi requirements -------------------
fswebcam,<br />
Ngrok,<br />
Golang,<br />
