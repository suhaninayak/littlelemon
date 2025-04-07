from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from django.contrib import messages 
from .models import Menu

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your reservation has been made successfully!")
            return redirect('book')  # redirects to the same page after success
    return render(request, 'book.html', {'form': form})

def menu(request):
    # Fetch all menu items
    menu_items = Menu.objects.all()

    # Define the preferred category order
    category_order = ["Starter", "Main Course", "Pizza", "Beverage", "Dessert"]
    # Group items by category in the desired order
    grouped_menu = {category: [] for category in category_order}  # Initialize empty lists

    for item in menu_items:
        category_display = item.get_category_display()  # Get readable category name
        if category_display in grouped_menu:  # Only add known categories
            grouped_menu[category_display].append(item)

    # Remove empty categories
    grouped_menu = {k: v for k, v in grouped_menu.items() if v}

    return render(request, 'menu.html', {"menu": grouped_menu})  # Pass structured menu



def display_menu_item(request, pk=None): 
    menu_item = get_object_or_404(Menu, pk=pk) if pk else None
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 
