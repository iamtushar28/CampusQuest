from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from custom_admin.forms import QuestionPaperForm, CustomLoginForm


#Login page view
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomLoginForm()
    
    return render(request, 'custom_admin/login.html', {'form': form})


#Dashboard page view
@login_required
def dashboard(request):
    return render(request, 'custom_admin/dashboard.html')


#Logout button
def custom_logout(request):
    logout(request)
    return redirect('custom_login')


#Upload question paper page view
@login_required
def add_question_paper(request):
    if request.method == 'POST':
        form = QuestionPaperForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Question paper uploaded successfully!')
            return redirect('add_question_paper')  # Redirect back to the form page
    else:
        form = QuestionPaperForm()
    return render(request, 'custom_admin/add_question_paper.html', {'form': form})    

