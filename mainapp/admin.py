from django.contrib import admin
from .models import Users,ThirdPlatformAccount,Mission,Chat
# Register your models here.

admin.site.register(Users)
admin.site.register(ThirdPlatformAccount)
admin.site.register(Mission)
admin.site.register(Chat)
