from .models import Message
from users.models import User
from django.db.models import Count

def get_all_messages():
    all_users = User.objects.filter(is_customer=True).values_list('id',flat=True)
    messages = []
    for user in all_users:
        message_obj = Message.objects.filter(customer__user_id=user).order_by('-date').values('customer__is_occupied', 'customer__user_id','value','date')[0]
        message_obj['username'] = User.objects.get(id=user).username
        messages.append(message_obj)
    print(messages)
    return messages
    pass