from django.utils import timezone
from ..models import Blog, Category, Comment, Gallery, History, Project
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "blog", "parent", "status", "created_at"]
        read_only_fields = ["created_at"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class GallerySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        project_id = self.context["project_id"]
        return Gallery.objects.create(project_id=project_id, **validated_data)

    class Meta:
        model = Gallery
        fields = ["id", "image"]


class ProjectListSerializer(serializers.ModelSerializer):
    slug_id = serializers.ReadOnlyField()
    gallery = GallerySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "category",
            "created_at",
            "gallery",
            "slug_id",
        ]
        read_only_fields = ["created_at"]


class ProjectDetailSerializer(serializers.ModelSerializer):
    slug_id = serializers.ReadOnlyField()
    gallery = GallerySerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "category",
            "size",
            "dimensions",
            "scale",
            "created_at",
            "gallery",
            "slug_id",
        ]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        galleries_data = validated_data.pop("gallery", [])
        project = Project.objects.create(**validated_data)
        for gallery_data in galleries_data:
            Gallery.objects.create(project=project, **gallery_data)
        return project

    def update(self, instance, validated_data):
        galleries_data = validated_data.pop("gallery", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if galleries_data is not None:
            instance.gallery.all().delete()
            for gallery_data in galleries_data:
                Gallery.objects.create(project=instance, **gallery_data)

        return instance


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "description",
            "summary",
            "slug_id",
        ]


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "summary",
            "body",
            "is_published",
            "created_at",
            "updated_at",
            "slug_id",
            "comments",
        ]

class HistorySerializer(serializers.ModelSerializer):
    timestamp = serializers.DateField(required=False, allow_null=True)
    class Meta:
        model = History
        fields = ["id", "action", "timestamp"]
        read_only_fields = ["id"]
        
    def validate_timestamp(self, value):
        if value in [None, ""]:
            return timezone.now().date()
        return value
