from django.contrib import admin
from atexit import register
from application.models import *


# Register your models here.

admin.site.register(contact_table)
admin.site.register(book_table)
admin.site.register(event_table)
