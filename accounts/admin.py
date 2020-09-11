from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Verification)
admin.site.register(Contact)


admin.site.site_header='CORPAD ADMIN'
admin.site.site_title='CORPAD ADMIN'