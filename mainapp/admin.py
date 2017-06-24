from django.contrib import admin
from .models import Users,ThirdPlatformAccount,Mission,Chat,Activity,Advertisement
# Register your models here.

admin.site.register(Users)
admin.site.register(ThirdPlatformAccount)
admin.site.register(Mission)
admin.site.register(Chat)
admin.site.register(Activity)
admin.site.register(Advertisement)
