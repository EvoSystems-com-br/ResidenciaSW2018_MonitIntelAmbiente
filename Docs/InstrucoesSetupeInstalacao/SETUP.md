# Setup guide of Monitoramento Inteligente de Ambientes project

## 1. Object detection
From `Código-fonte/object-detection`, do:
1. Install Nvidia CUDA-9.0, following this [tutorial](https://yangcha.github.io/CUDA90/)
2. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
3. Activate virtualenv `$ source venv/bin/activate`
4. Install requirements `$ pip install -r requirements.txt`
5. Download YOLO pre-trained weight file `$ wget https://pjreddie.com/media/files/yolov3.weights -P weights/`
6. TODO (set IPs instructions)

## 2. Actions
From `Código-fonte/actions`, do:
1. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
2. Activate virtualenv `$ source venv/bin/activate`
3. Install requirements `$ pip install -r requirements.txt`
4. Set up boto3 authentication credentials, following the [Boto 3 Docs](https://boto3.readthedocs.io/en/latest/guide/quickstart.html#installation)
5. Set valid and verified (by Amazon SES) e-mail adress to sender and receiver

## 3. Fainting recognition
From `Código-fonte/fainting-recognition`, do:
1. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
2. Activate virtualenv `$ source venv/bin/activate`
3. Install requirements `$ pip install -r requirements.txt`

## 4. Video submission
1. Clone [python-live-video-streaming](https://github.com/jhonata-antunes/python-live-video-streaming) repo into a Raspberry Pi with camera. It contains the video streaming.
2. Install OpenCV library `$ sudo apt-get install libopencv-dev python-opencv`
3. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
4. Activate virtualenv `$ source venv/bin/activate`
5. Install requirements `$ pip install -r requirements.txt`

## 5. Install message broker
- Run `sudo apt-get install mosquitto`