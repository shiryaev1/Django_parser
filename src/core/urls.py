from core.views import HSCodeViewSet, HSCodeCategoryViewSet, HSCodeSubcategoryViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'hs_codes', HSCodeViewSet, basename='hs_codes')
router.register(r'hs_codes_category', HSCodeCategoryViewSet, basename='hs_codes_category')
router.register(r'hs_codes_subcategory', HSCodeSubcategoryViewSet, basename='hs_codes_subcategory')
urlpatterns = router.urls
