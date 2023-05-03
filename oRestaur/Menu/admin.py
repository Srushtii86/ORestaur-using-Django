from django.contrib import admin
from .models import OMenu
from .models import Sides
from .models import Appetizer
from .models import MainCourse
from .models import Dessert

admin.site.register(OMenu)
admin.site.register(Sides)
admin.site.register(Appetizer)
admin.site.register(MainCourse)
admin.site.register(Dessert)

