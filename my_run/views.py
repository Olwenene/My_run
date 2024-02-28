from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from .models import Question
from .form import Choiceform

def register(request):
    """ 
    defining a function to register a user with a form provided.
    """
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_run:login')
 
    return  render(request, 'register.html', {'form': form})
    
def user_login(request):
    """ 
    A function to login users.
    """
    return render(request, 'login.html')

def authenticate_user(request):
    """ 
    This function authenticate the user and then provide them with the appropriate next step depending on their outcome.
    """
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
    """ 
    A function that provides the user with the question form.
    """
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'detail.html', {'question':question})
    
def vote(request):
    """ 
    A function that allows the user to vote for their desired  candidate.
    """
    if request.method == 'POST':
        form = Choiceform(request.POST)
        if form.is_valid():
            form.save(commit=False)
        return redirect('my_run:goodbye')        
    else:
        form = Choiceform()
    return render(request, 'detail.html', {'form': form})

def goodbye(request):
    """ 
    This function provides the user with a an appreciation message.
    """
    return render(request, 'goodbye.html')

