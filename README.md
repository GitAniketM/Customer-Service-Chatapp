# Customer-Service-Chatapp
This is a customer service chatapp developed using django which allows the user and agent to communicate between each other live and it also allows the agent to view list of queries that have been generated by the user and reply to them. 

I have enabled system so that if one user have been replied by some agent then when other agent opens the page of queries generated by user, he/she wont be able to click and respond since that user has already been occupied by some agent.

## Primary Tech Stack Used:
1. Django
2. Django Channels
3. Channels Redis
4. Web Socket

------------------------
## Installation Process:

-  First clone the github repository to your computer by running the following command:
```shell
git clone <repository_link>
```

- Then go to that repository and run the following commands line by line(For windows):
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations chat users agents 
python manage.py migrate

python manage.py runserver 
```
This will run a local server at ```localhost:8000``` and through that you can access the project.
