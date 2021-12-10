from django.contrib import admin

#register all of the models here

from .models import Topic

from .models import Entry

admin.site.register(Topic)

admin.site.register(Entry)