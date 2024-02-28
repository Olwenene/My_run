from django.urls import path
from . import views

app_name = 'my_run'
urlpatterns = [
    path('', views.register, name="register"),
    path('login/', views.user_login, name="login"),
    path('authenticate/', views.authenticate_user, name="authenticate"),
    path('vote/', views.vote, name='vote'),
    path('detail/<int:pk>/', views.question_detail, name='question_detail'),
    path('goodbye/', views.goodbye, name="goodbye")
]

