from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_auth, name="agent_auth"),
    path('detail_page/', views.detailPage, name="chat_detail_page"),
    path('detail_page/update_occupancy/', views.updateOccupancy, name="chat_update_occupancy"),
    path('login/', views.agent_login, name="agent_login"),
]
