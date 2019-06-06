from rest_framework import routers
from .views import UserView

router = routers.DefaultRouter()
router.register(r'accounts', UserView, 'list')

urlpatterns = router.urls
