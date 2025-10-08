from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

from .validators import validate_file_size


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("عنوان"))
    slug = models.SlugField(unique=True, verbose_name=_("اسلاگ"))
    description = models.TextField(verbose_name=_("توضیحات"))
    summary = models.TextField(verbose_name=_("خلاصه"))
    body = RichTextField(verbose_name=_("متن"))
    is_published = models.BooleanField(default=True, verbose_name=_("منتشر شده"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاریخ بروزرسانی"))

    class Meta:
        verbose_name = _("بلاگ")
        verbose_name_plural = _("بلاگ‌ها")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        super().save(*args, **kwargs)

    @property
    def slug_id(self):
        return f"{self.slug}-{self.id}"

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(verbose_name=_("متن"))
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name=_("بلاگ"))
    parent = models.ForeignKey(
        "self", null=True, on_delete=models.CASCADE, verbose_name=_("پدر")
    )
    status = models.BooleanField(default=True, verbose_name=_("وضعیت"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("تاریخ بروزرسانی"))
    class Meta:
        verbose_name = _("کامنت")
        verbose_name_plural = _("کامنت‌ها")


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("دسته‌بندی")
        verbose_name_plural = _("دسته‌بندی‌ها")


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("عنوان"))
    slug = models.SlugField(unique=True, verbose_name=_("اسلاگ"))
    description = models.TextField(verbose_name=_("توضیحات"))
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name=_("دسته‌بندی")
    )
    size = models.PositiveIntegerField(verbose_name=_("اندازه"))
    dimensions = models.CharField(max_length=30, verbose_name=_("ابعاد"))
    scale = models.PositiveIntegerField(verbose_name=_("مقیاس"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def slug_id(self):
        return f"{self.slug}-{self.id}"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("پروژه")
        verbose_name_plural = _("پروژه‌ها")


class Gallery(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery",
        verbose_name=_("پروژه"),
    )
    image = models.ImageField(
        upload_to="content/images",
        validators=[validate_file_size],
        verbose_name=_("تصویر"),
    )

    class Meta:
        verbose_name = _("گالری")
        verbose_name_plural = _("گالری‌ها")
        
        
class History(models.Model):
    action = models.CharField(max_length=100, verbose_name=_("عملیات"))
    timestamp = models.DateField(default=timezone.now, verbose_name=_("زمان"))

    class Meta:
        verbose_name = _("تاریخچه")
        verbose_name_plural = _("تاریخچه‌ها")
