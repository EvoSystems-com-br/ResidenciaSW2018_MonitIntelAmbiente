# User management service


### Setup
1. Create virtualenv `$ virtualenv --system-site-packages -p python3 venv`
2. Activate virtualenv `$ source venv/bin/activate`
3. Install requirements `$ pip install -r requirements.txt`
4. Set the variable `USER_SERVER` (`users/service/settings.py`) 

### Run
`$ python3 service/manage.py makemigrations`  
`$ python3 service/manage.py migrate`  
`$ python3 service/manage.py runserver <USER_SERVER>:8080`

### API
|    Function    | Method |       URL      |       Parameters (Request Body)       |
|:--------------:|:------:|:--------------:|:-------------------------------------:|
|      list      |   GET  |    /cameras/   |                                       |
|     create     |  POST  |    /cameras/   |    id, model_name, [address], user    |
|      read      |   GET  | /cameras/{id}/ |                                       |
|     update     |   PUT  | /cameras/{id}/ |    id, model_name, [address], user    |
| partial_update |  PATCH | /cameras/{id}/ | [id], [model_name], [address], [user] |
|     delete     | DELETE | /cameras/{id}/ |                                       |

|    Function    | Method |     URL     |                  Parameters (Request Body)                 |
|:--------------:|:------:|:-----------:|:----------------------------------------------------------:|
|      list      |   GET  |   /users/   |                                                            |
|     create     |  POST  |   /users/   |     email, password, name, [last_name], cpf, [address]     |
|      read      |   GET  | /users/{id} |                                                            |
|     update     |   PUT  | /users/{id} |     email, password, name, [last_name], cpf, [address]     |
| partial_update |  PATCH | /users/{id} | [email], [password], [name], [last_name], [cpf], [address] |
|     delete     | DELETE | /users/{id} |                                                            |

### Usage examples
- Running  
`$ python3 service/manage.py runserver 127.0.0.1:8080`  
- Create a user (as a staff user)  
`$ python3 service/superuser.py` 
- Create a user  
![Alt text](service/create_user_sample.png?raw=true "User creation")
