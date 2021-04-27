from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
def _redirect(request, url):
    nxt = request.GET.get("next", None)
    if nxt is not None:
        url=index
    return redirect(url)
@login_required
def index(request):
    return _redirect(request, 'polls/')
def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'polls/index.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)