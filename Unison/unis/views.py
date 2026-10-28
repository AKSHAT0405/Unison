from django.shortcuts import render
from .models import unis
from .forms import UnisForm , UserRegistrationForm
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login 
# Create your views here.
def index(request):
    return render(request , 'index.html')

def unis_list(request):
    uniss = unis.objects.all().order_by('-created_at')
    return render(request, 'unis_list.html' , {
        'uniss' : uniss
    })

@login_required
def unis_create(request):
    if request.method == "POST":
        form = UnisForm(request.POST , request.FILES)
        if form.is_valid():
            Unis = form.save(commit=False)
            Unis.user = request.user
            Unis.save()
            return redirect('unis_list')
    else:
        form = UnisForm()

    return render(request , 'unis_form.html' , {
        'form':form
    })

@login_required
def unis_edit(request , Unis_id):
    unis_obj = get_object_or_404(unis, pk = Unis_id , user = request.user)
    if request.method == "POST":
        form = UnisForm(request.POST , request.FILES , instance=unis_obj)
        if form.is_valid():
            Unis = form.save(commit=False)
            Unis.user = request.user
            Unis.save()
            return redirect('unis_list')
    else:
        form = UnisForm(instance=unis_obj)

    return render(request , 'unis_form.html' , {
    'form':form
    })

@login_required
def unis_delete(request , Unis_id):
    unis_obj = get_object_or_404(unis , pk = Unis_id , user = request.user)
    if request.method == 'POST':
        unis_obj.delete()
        return redirect('unis_list')
    
    return render(request , 'unis_confirm_delete.html' , { 'unis' : unis_obj }) 

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request , user)
            return redirect('unis_list')
    else:
        form = UserRegistrationForm()
    return render(request , 'registration/register.html' , { 'form' : form }) 
