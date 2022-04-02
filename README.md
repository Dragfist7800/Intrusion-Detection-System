# Intrusion-Detection-System
This is a system for detecting home intrusion .

## System Operations
Initially Images are captured using CCTV camera connected to the Raspberry pi, then the images from the Raspberry pi will be sent to an AWS Windows VM (capturing and sending images from linux to windows is done through a bash script). 
The VM itself has UiPath studio running with the necessary python ML models. Each image being captured will be sent to the VM running UiPath for movement and object detection. It is necessary to train the faces of the householders for the model to classify them as safe, additionally it can also identify animals and birds if the customer wishes, so there is no gap for false alerts. If an unregistered face is detected, it tries to take images of their face and sends an e-mail to the owner of the household for further confirmation. If the owner identifies them as an intruder, the bot provides options to contact emergency numbers or police directly and can inform about the incident.


## Hardware and Software requirements
### Hardware:
Rasperry pi
cctv camera

### Software:
### Base ----------------------------------------
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.2
Pillow>=7.1.2
PyYAML>=5.3.1
requests>=2.23.0
scipy>=1.4.1
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0

### Logging -------------------------------------
tensorboard>=2.4.1
### wandb

### Plotting ------------------------------------
pandas>=1.1.4
seaborn>=0.11.0

### Face-recognition ----------------------------
dlib
face_recognition
cmake for face-recognition download the .msi file and install with path set. Use this link to download https://cmake.org/download/

### Raspberry pi requirements -------------------
fswebcam,
Ngrok,
Golang,
