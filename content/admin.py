from django.contrib import admin

from django.contrib import admin
from .models import Blog, Comment, Category, Project, Gallery


# ---------- Inline Classes ----------
class CommentInline(admin.TabularInline):   # نمایش کامنت‌ها داخل صفحه Blog
    model = Comment
    extra = 1
    fields = ("text", "status", "created_at")
    readonly_fields = ("created_at",)


class GalleryInline(admin.TabularInline):   # نمایش گالری داخل صفحه Project
    model = Gallery
    extra = 1


# ---------- Admin Classes ----------
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "created_at", "updated_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title", "description", "summary")
    prepopulated_fields = {"slug": ("title",)}  
    ordering = ("-created_at",)
    inlines = [CommentInline]
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": ("title", "slug", "is_show")
        }),
        ("متن و توضیحات", {
            "fields": ("summary", "description", "body")
        }),
        ("زمان‌ها", {
            "fields": ("created_at", "updated_at")
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "blog", "parent", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("text",)
    autocomplete_fields = ("blog", "parent")
    readonly_fields = ("created_at",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "size", "scale", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [GalleryInline]
    readonly_fields = ("created_at",)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("project", "image")
    autocomplete_fields = ("project",)

