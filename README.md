
# StoreInventorySystem
Ubuntu 16.04
StoreInventorySystem API:
API signature:
http://0.0.0.0:8001/storeappsinup
Request Type- Post
Request Response:

    {
    "created": "2018-08-07T15:31:37.975760Z",
    "username": "goldy",
    "email": "goldy@gmail.com",
    "password": "pushp",
    "is_manager": true,
    "is_assistant": false
    }
    
Setup and installation
Run following cammand
sudo apt-get update

Install python package
application



server {
    listen 8000;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/sss/Documents/StoreInventorySystem/project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/sss/Documents/StoreInventorySystem/project/project.sock;
    }
}
Run following cammand
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
