from django.contrib import admin
from . import models
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    # change the default order of the fields
    fields = ["release_year", "length", "title"]

    search_fields = ["title", "length"]

    list_filter = ["release_year", "length"]

    list_display = ["release_year", "length", "title"]
    # note: editable fields needs to be displayed as well
    list_editable = ["length"]


 # then register to admin site like this
admin.site.register(models.Movie, MovieAdmin) 

admin.site.register(models.Customer)
