from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrderForm, CreateUserForm
from .models import MyData

# Create your views here.

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('/')
		context = {'form':form}
		return render(request, 'app/register.html', context)
        
	
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    user = request.user
    obj = MyData.objects.filter(user=user)
    return render(request, 'app/index.html', {'obj': obj})


@login_required(login_url='login')
def createdata(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        data = request.POST.get('content')
        userdata = MyData(user=user, title=title, data=data)
        userdata.save()
        return redirect('/')


@login_required(login_url='login')
def getdata(request):
    if request.method == 'GET':
        obj = MyData.objects.all()
        print(obj)
        return redirect('/')


@login_required(login_url='login')
def deletedata(request, id):
    if request.method == 'POST':
        MyData.objects.filter(id=id).delete()
    return redirect('/')

@login_required(login_url='login')
def search(request):
    query = request.GET.get('query')
    alldata=MyData.objects.all()
    searchData=[]
    print(query)
    if len(query)==0:
        return redirect('/')
    if len(query)>80:
        searchData = []
    else:
        for i in range(len(alldata)):
            if query in alldata[i].title or query in alldata[i].data:
                print(alldata[i])
                searchData.append(alldata[i])
    if searchData.count==0:
        messages.warning(request,"No search Found please refine your search ")
    print(searchData)
    return render(request,'app/search.html',{'searchData':searchData, 'query': query})
