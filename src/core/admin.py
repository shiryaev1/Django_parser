from django.contrib import admin
from core.models import (
    HSCode,
    HSCodeCategory,
    HSCodeSubcategory
    )


admin.site.register(HSCodeCategory)
admin.site.register(HSCodeSubcategory)
admin.site.register(HSCode)

