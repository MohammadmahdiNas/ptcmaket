from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet, basename="categories")
router.register("blogs", views.BlogViewSet, basename="blogs")
router.register("projects", views.ProjectViewSet, basename="projects")
# router.register('galleries', GalleryViewSet, basename='galleries')
# router.register('comments', CommentViewSet, basename='comments')

projects_router = routers.NestedDefaultRouter(router, "projects", lookup="project")
projects_router.register( 
    "galleries", views.GalleryViewSet, basename="project-galleries"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(projects_router.urls))
]
