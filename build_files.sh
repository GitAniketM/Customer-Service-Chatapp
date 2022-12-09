pip3 install -r requirements.txt
python3.9 manage.py makemigrations chat agents users --noinput
python3.9 manage.py migrate --noinput
python3.9 manage.py collectstatic --noinput --clear
