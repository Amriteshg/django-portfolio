from django.contrib import admin
from .models import *
from .views import *

admin.site.register(About)
admin.site.register(Skill)
admin.site.register(CodeSkill)
admin.site.register(SoftSkill)
admin.site.register(RecentWork)
admin.site.register(Contact)
admin.site.register(MyIcon)