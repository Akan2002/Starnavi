from django.contrib import admin
from mainapp.models import(
    User, SmsUser
)
admin.site.register(User)
admin.site.register(SmsUser)

