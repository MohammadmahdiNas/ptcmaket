from django.shortcuts import get_object_or_404, render
from ..models import Blog, Category, Project, Gallery, Comment
from .serializers import *
from rest_framework.viewsets import ModelViewSet, GenericViewSet


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "slug_id"

    def get_object(self):
        slug_id = self.kwargs.get(self.lookup_field)
        slug, pk = slug_id.rsplit("-", 1)
        return get_object_or_404(Category, pk=pk)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    lookup_field = "slug_id"

    def get_object(self):
        slug_id = self.kwargs.get(self.lookup_field)
        slug, pk = slug_id.rsplit("-", 1)
        return get_object_or_404(Blog, pk=pk)

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            return BlogListSerializer(*args, **kwargs)
        return BlogDetailSerializer(*args, **kwargs)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all().prefetch_related("gallery")
    serializer_class = ProjectDetailSerializer
    lookup_field = "slug_id"

    def get_object(self):
        slug_id = self.kwargs.get(self.lookup_field)
        slug, pk = slug_id.rsplit("-", 1)
        return get_object_or_404(Project.objects.prefetch_related("gallery"), pk=pk)

    def get_serializer(self, *args, **kwargs):
        if self.action == "list":
            return ProjectListSerializer(*args, **kwargs)
        return super().get_serializer(*args, **kwargs)


from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import get_object_or_404
# Assume Project, Gallery, GallerySerializer are defined elsewhere

class GalleryViewSet(ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def get_serializer_context(self):
        # 1. Start by calling the super method to get the base context
        context = super().get_serializer_context() 
        
        # The key for the parent lookup is typically prepended/renamed by NestedDefaultRouter
        # Using 'slug_id_slug_id' based on the router configuration
        slug_id = self.kwargs.get("project_slug_id") 

        if slug_id:
            # Safely split the slug and the primary key
            # Example: "modern-villa-1" -> slug="modern-villa", pk="1"
            slug, pk = slug_id.rsplit("-", 1)
            context["project_id"] = pk
        else:
            # Provide a fallback value if the slug_id is missing (e.g., for schema generation or if routing fails)
            context["project_id"] = None 
            
        return context

    def get_queryset(self):
        # The key for the parent lookup is used to filter the Gallery objects
        slug_id = self.kwargs.get("project_slug_id") 

        if not slug_id:
            # If the required parameter is missing, return an empty queryset
            return Gallery.objects.none()
        
        # Safely split the slug and the primary key
        slug, pk = slug_id.rsplit("-", 1)
        
        # Filter galleries by the extracted project primary key (pk)
        return Gallery.objects.filter(project_id=pk)
