from django.contrib import admin
from .models import *
@admin.register(IssuedBook)
class VenueAdmin(admin.ModelAdmin):
    list_display=('student_id','isbn','issued_date','expiry_date')
admin.site.register(Book)
admin.site.register(Student)
#admin.site.register(IssuedBook)