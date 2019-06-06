from .views import ReviewView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ReviewView)
# app_name will help us do a reverse look-up latter.
urlpatterns = router.urls
