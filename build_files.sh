sudo apt install sqlite-devel
pip3 install -r requirements.txt
python3.9 manage.py collectstatic
python3.9 manage.py makemigrations chat agents users
python3.9 manage.py migrate
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'password')" | python manage.py shell