from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if user.user_type == 1:
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    return render(request, 'login.html')

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})
