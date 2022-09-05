from django.shortcuts import render
from product.models import Product


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.shortcuts import render, redirect

# Create your views here.


def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    context = {
        'newest_products': newest_products,
    }
    return render(request, 'core/frontpage.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) or None
        if form.is_valid():
            username = request.POST.get('username')

            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form, 'title': 'reqister here'})

###################################################################################
################login forms###################################################


def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect('/')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form, 'title': 'log in'})


def contactpage(request):
    return render(request, 'core/contact.html')
