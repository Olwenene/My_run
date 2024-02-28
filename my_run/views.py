from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from .models import Question
from .form import Choiceform

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_run:login')
 
    return  render(request, 'register.html', {'form': form})
    
def user_login(request):
    return render(request, 'login.html')

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            question_objects = Question.objects.all()
            context = {"question_objects": question_objects}
            return render(request, 'question.html', context)
        else:
            return render(request, 'register.html', {'error_message': 'Invalid credentials'})

    return render(request, 'register.html')

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'detail.html', {'question':question})
    
def vote(request):
    if request.method == 'POST':
        form = Choiceform(request.POST)
        if form.is_valid():
            form.save(commit=False)
        return redirect('my_run:goodbye')        
    else:
        form = Choiceform()
    return render(request, 'detail.html', {'form': form})

def goodbye(request):
    return render(request, 'goodbye.html')

