from modeltranslation.translator import TranslationOptions, register

from .models import Blog, Category, History, Project


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ["title", "slug"]


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ["title", "slug", "description"]


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ["title", "slug", "description", "summary", "body"]


@register(History)
class HistoryTranslationOptions(TranslationOptions):
    fields = ["action"]