from django.contrib import admin

# Register your models here

from .models.area import Area, AccessArea
from .models.indicator import Indicator, Indicator1
from .models.tag import Tag, TagN
from .models.column import Column
from .models.school import BachelorProgramInfo, ProfessionalPractice, Pvvc
from .models.user import User



admin.site.register(Indicator)
admin.site.register(Indicator1)
admin.site.register(BachelorProgramInfo)
admin.site.register(ProfessionalPractice)
admin.site.register(Pvvc)
admin.site.register(Tag)
admin.site.register(TagN)
admin.site.register(Column)
admin.site.register(Area)
admin.site.register(AccessArea)
admin.site.register(User)



