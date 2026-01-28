from django.shortcuts import render, redirect
from .forms import Reservationform, Reservationpageform
from .models import MenuItem, Category
from django.contrib import messages

def home_page(request):
    # Handle reservation form submission
    if request.method == 'POST':
        form = Reservationform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been made successfully!')
            return redirect('index')
        else:
            messages.error(request, 'There was an error with your reservation. Please check the form and try again.')
    else:
        form = Reservationform()

    # Fetch menu items and categories for menu partial
    menu_items = MenuItem.objects.all()
    categories = Category.objects.all()

    context = {
        'form': form,
        'menu_items': menu_items,
        'categories': categories,
    }
    messages.success(request, "Data saved successfully!")
    return render(request, 'index.html', context)


def about_page(request):
    return render(request, 'about.html')

def menu_page(request):
    menu_items = MenuItem.objects.all()
    categories = Category.objects.all()
    context = {
        'menu_items': menu_items,  # pass them to the template
        'categories': categories,
    }
    return render(request, 'menu.html', context)
 
def reservation_page(request):
    if request.method == 'POST':
        form = Reservationpageform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been made successfully!')   
            return redirect('index')
        else:
            messages.error(request, 'There was an error with your reservation. Please check the form and try again.')
    else: #GET request
        form = Reservationpageform() 

    return render(request, 'book.html', {'form': form })  