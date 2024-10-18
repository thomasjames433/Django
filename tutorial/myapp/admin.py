#admin username thomas password ksi

from django.contrib import admin
from .models import Footballer

# Register your models here.

admin.site.register(Footballer)