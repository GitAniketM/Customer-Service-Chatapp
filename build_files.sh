pip3 install -r requirements.txt
python3.9 manage.py collectstatic
python3.9 manage.py makemigrations chat agents users
python3.9 manage.py migrate