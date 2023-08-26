from rest_framework.routers import DefaultRouter
from .views import NoteViewset

router = DefaultRouter()
router.register("notes", NoteViewset)

urlpatterns = router.urls