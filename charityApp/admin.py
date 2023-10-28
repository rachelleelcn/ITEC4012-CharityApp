from django.contrib import admin
from .models import Charity
from .models import Community
from .models import User_History
from .models import User_Community
from .models import Community_History
from .models import Community_Charity
from .models import Community_Comment

# Register your models here.
admin.site.register(Charity)
admin.site.register(Community)
admin.site.register(User_History)
admin.site.register(User_Community)
admin.site.register(Community_History)
admin.site.register(Community_Charity)
admin.site.register(Community_Comment)
