from django.contrib import admin

# Models get registered here.
from .models import Session
from .models import Location
from .models import Attendant

admin.site.register(Session)
admin.site.register(Location)
admin.site.register(Attendant)
