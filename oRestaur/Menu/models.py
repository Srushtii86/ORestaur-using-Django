from django.db import models

class OMenu(models.Model):
    __slots__ = ()
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length = 2048)
    cover_url = models.CharField(max_length=2048)

    def __str__(self):
        return self.title

class Sides(OMenu):
    __slots__ = ()

class Appetizer(OMenu):
    __slots__ = ()

class MainCourse(OMenu):
    __slots__ = ()

class Dessert(OMenu):
    __slots__ = ()
