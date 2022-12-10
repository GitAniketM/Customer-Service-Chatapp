import json
from django.shortcuts import render, redirect
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.http import JsonResponse
from users.models import User
from django.contrib.auth import login as django_login

# Create your views here.
def auth(request):
    print(request.user.username)
    return render(request, 'auth.html')

@csrf_exempt
def login(request):
    try:
        if request.method == 'POST':
            
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            user = User.objects.get(username=username)
            print(User.objects.filter(username=username, password=password).exists())
            # if check_password(password, user.password):
            if User.objects.filter(username=username, password=password).exists():
                print("checked password allowing login")
                django_login(request, user)
                return JsonResponse({'status':'success', 'message':'logged in successfully', 'error':False}, status=200)
            
            messages.warning(request, "log in unsuccessful please try again")
            return redirect('auth')
    except Exception as e:
        print(e)
        return json.dumps({'status':'failed', 'message':'Something weird happened. We are looking into it.', 'error':True})    
    
@csrf_exempt
def signup(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            password = data.get('password')
            
            if User.objects.filter(username=username).exists():
                messages.warning(request, "Username already exists. Please try signing in with different name")
                return redirect('auth')
            
            user = User(username=username, password=password, is_customer = True)
            user.save()
            django_login(request, user)
            c, _ = Customer.objects.get_or_create(user=user)
            return json.dumps({'status':'success','message':'Signed up successfully','error':False})
    
    except Exception as e:
        print(e)
        return JsonResponse({'status':'failed', 'message':'Something weird happened. We are looking into it.', 'error':True}, status = 500) 
        