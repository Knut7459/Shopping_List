from django.shortcuts import render
from .models import ShoppingItem

# Create your views here.
def mylist(request):
    if request.method == 'POST':
        print('Received Data:', request.POST['itemName'])
        ShoppingItem.objects.create(P_Name = request.POST['itemName'])
    all_items = ShoppingItem.objects.all()
    
    return render(request,'shopping_list.html',{'all_items':all_items})