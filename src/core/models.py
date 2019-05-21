from django.db import models
import uuid


class HSCodeCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=120)


class HSCodeSubcategory(models.Model):
    subcategory_name = models.CharField(max_length=120)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hs_code_category = models.ForeignKey(HSCodeCategory, on_delete=models.CASCADE)


class HSCode(models.Model):
    code = models.CharField(max_length=8)
    description = models.CharField(max_length=120)
    short_description = models.CharField(max_length=120)
    hs_code_subcategory = models.ForeignKey(HSCodeSubcategory, on_delete=models.CASCADE)
