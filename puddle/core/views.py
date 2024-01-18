<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
>>>>>>> 17ae6f9d22daac6957a28e2483c560d91e9d2423
from item.models import Category, Item

from .forms import SignupForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html',{
        'categories':categories,
        'items':items,
        })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    form = SignupForm()
<<<<<<< HEAD
=======
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
        
>>>>>>> 17ae6f9d22daac6957a28e2483c560d91e9d2423

    return render(request, 'core/signup.html', {
        'form':form
    })
