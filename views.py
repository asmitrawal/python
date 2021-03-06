from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import PasswordResetForm, AuthenticationForm
from book.models import Laptops
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        #import ipdb
        #ipdb.set_trace()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('login')

    else:
        form = RegisterForm()
    context = {"form": form}
    return render(request, 'userapp/register.htm', context)

def user_login(request):
    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        #import ipdb
        #ipdb.set_trace()
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('laptop-list')
            else:
                messages.error(request,"You are not registered")

        else:
            messages.error(request,"Invalid credentials")
    form = AuthenticationForm()
    return render(request, 'userapp/login.htm',{'form':form})

def user_logout(request):
    logout(request)
    messages.info(request,"successfully logged out")
    return redirect("register")

def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "userapp/password-reset-email.txt"
                    c = {
                    "email":user.email,
                    'domain':'127.0.0.1:8000',
                    'site_name': 'Website',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    'token': default_token_generator.make_token(user),
                    'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'rawal.asmit@gmail.com' , [user.email], fail_silently=False)
                        return redirect ("login")
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                        #messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                        #return redirect ("/")
            #messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()

    return render(request=request, template_name="userapp/password-reset-form.htm", context={"password_reset_form":password_reset_form})