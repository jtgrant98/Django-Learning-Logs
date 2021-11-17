from django.contrib import admin
from .models import Entry

# Register your models here.
from .models import Topic

admin.site.register(Topic)
admin.site.register(Entry)