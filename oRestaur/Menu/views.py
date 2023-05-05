from django.shortcuts import render
from .models import OMenu,Sides,Appetizer,MainCourse,Dessert

def menu_view(request):
    omenu = {'menu': OMenu.objects.all()}
    side = {'sides' : Sides.objects.all()}
    appetizer = {'appetizers' : Appetizer.objects.all()}
    main = {'maincourse' : MainCourse.objects.all()}
    dessert = {'dessert' : Dessert.objects.all()}
    elements = {
        "A": omenu,
        "B" : side,
        "C" : appetizer,
        "D" : main,
        "E" : dessert
    }

    return render(request, 'Menu/index.html/', {"elements": elements})


