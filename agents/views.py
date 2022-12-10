import json
from django.shortcuts import render, redirect
from chat.utils import get_all_messages
from users.models import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from users.models import User
from .models import Agents

# Create your views here.
def detailPage(request):
    message_list = get_all_messages()
    try:
        customer_id = Agents.objects.get(agent_id = request.user.id).customer_id
    except:
        customer_id=""
    context = {
        'message_list':message_list,
        'customer_id': customer_id
    }
    return render(request, 'chat_detail.html', context=context)

@csrf_exempt
def updateOccupancy(request):
    try:
        if request.method == 'POST':
            print(request.user.username)
            data = json.loads(request.body.decode('utf-8'))
            is_occupant = data.get('is_occupied')
            username = data.get('username')
            c = Customer.objects.get(user__username = username)
            c.is_occupied = is_occupant
            
            u = User.objects.get(username=request.user.username, is_agent=True)
            a = Agents.objects.get(agent=u)
            a.customer = c
            a.save()
            
            c.save()
            
            return json.dumps({'status':'success', 'message':'Occupancy updated successfully'})
    except Exception as e:
        print("Error occured: ",e)
        
def agent_auth(request):
    return render(request, 'agent_auth.html')

@csrf_exempt
def agent_login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.get(username=username, password=password, is_agent=True)
        if user is not None:
            print("logged in successfully")
            login(request, user)
            return json.dumps({'status':'success', 'message':'Log in successful', 'error':False})
        
        return redirect("agent_login")
     
        
        