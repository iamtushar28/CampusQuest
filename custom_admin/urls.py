
from django.urls import path
from custom_admin import views

urlpatterns = [

    path('login/', views.custom_login, name='custom_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.custom_logout, name='custom_logout'),
    path('add-question-paper/', views.add_question_paper, name='add_question_paper'),
    
]
