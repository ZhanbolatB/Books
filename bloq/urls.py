from rest_framework.routers import DefaultRouter
from .views import AuthorModelViewSet, GenreModelViewSet, BookModelViewSet

router = DefaultRouter()

router.register('author', AuthorModelViewSet)
router.register('genre', GenreModelViewSet)
router.register('book', BookModelViewSet)

urlpatterns = router.urls