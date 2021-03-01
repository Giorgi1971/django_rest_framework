from django.contrib import admin
from .models import *
# Register your models here.
from snippets.models import Snippet

admin.site.register(Snippet)