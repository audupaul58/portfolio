from django.contrib import admin
from .models import Skills, About
# Register your models here.

admin.site.register([Skills, About])
