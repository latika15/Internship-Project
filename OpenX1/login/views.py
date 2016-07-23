from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.core.context_processors import csrf
from login.forms import RegistrationForm
from components.models import GovTable, BroadcastMessage
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def landing_view(request):
    try:
    	broadcast = BroadcastMessage.objects.all().order_by('-broadcast_date')[0]
    	broadcast_msg = broadcast.broadcast_msg
    except IndexError:
	broadcast_msg = ''
    context = {'broadcast_msg':broadcast_msg}
    return render_to_response('landing.html',context)

def login_view(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login/login.html', c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        if request.user.is_superuser:
            message_text = 'Welcome %s' % username
            messages.success(request, message_text)
            return HttpResponseRedirect('/admin')
        elif request.user.is_staff:
            official_type = GovTable.objects.get(username_id=request.user.id)
            print official_type.is_deptHead
            if official_type.is_superofficial:
                message_text = 'Welcome %s' % username
                messages.success(request, message_text)
                return HttpResponseRedirect('/gov')
            elif official_type.is_deptHead:
                message_text = 'Welcome %s' % username
                messages.success(request, message_text)
                return HttpResponseRedirect('/gov/dept/')
            else:
                message_text = 'Welcome %s' % username
                messages.success(request, message_text)
                return HttpResponseRedirect('/gov/official/')
        else:
            message_text = 'Welcome %s' % username
            messages.success(request, message_text)
            return HttpResponseRedirect('/customer/feed')
    else:
        #messages.error(request, 'Invalid details.Please login again with valid details.')
        return HttpResponseRedirect('/home/login/')
    
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')

def register_user_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered. Please login.')
            return render(request, 'login/login.html')
        
    args ={}
    args.update(csrf(request))
    
    args['form'] = RegistrationForm()
    print args
    return render(request, 'login/register.html', args)



    