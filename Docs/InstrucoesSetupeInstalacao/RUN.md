# Run guide of Monitoramento Inteligente de Ambientes project

## 1. Object detection
- From `Código-fonte/object-detection`, run the object detection service `$ python3 service/manage.py runserver <public IP>:<port>`

## 2. Actions
- From `Código-fonte/actions`, run the actions service `$ python3 service/manage.py runserver <public IP>:<port>`

## 3. Fainting recognition
- From `Código-fonte/fainting-recognition`, run fainting recognition service `$ python3 service.py`

## 4. Video submission
- From Raspberry Pi, start video submission, by running `$ python3 server.py --ip <object-detection IP> --port <object-detection port>`
- From any computer, inscrible a new video transmission, by running `$ curl --data "port=<port>". http://<object-detection IP>:<object-detection port>/object-detection/register/`