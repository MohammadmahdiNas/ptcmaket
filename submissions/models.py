from django.utils import timezone
from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    description = models.TextField(verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "ارتباط"
        verbose_name_plural = "ارتباطات"


class Apply(models.Model):
    STATUS_CHOICES = [
        (
            "pending",
            "pending",
        ),  # first is name in database seccond is name for display in admin or site
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]

    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    education_degree = models.CharField(max_length=30, verbose_name="مقطع تحصیلی")
    study_field = models.CharField(max_length=30, verbose_name="رشته تحصیلی")
    resume = models.FileField(upload_to="resumes/", verbose_name="رزومه")
    cover_letter = models.TextField(verbose_name="نامه پیوست")
    status = models.CharField(
        max_length=10,  # ex rejected
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name="وضعیت",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "درخواست"
        verbose_name_plural = "درخواست‌ها"


class Order(models.Model):
    company_name = models.CharField(max_length=50, verbose_name="نام شرکت")
    activity_area = models.CharField(max_length=50, verbose_name="حوزه فعالیت")
    email = models.EmailField(verbose_name="ایمیل")
    contact_number = models.CharField(max_length=15, verbose_name="شماره تماس")
    explanation = models.TextField(verbose_name="توضیحات")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    STATUS_CHOICES = [
        ("pending", "pending"),
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]
    status = models.CharField(
        max_length=10,  # ex rejected
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name="وضعیت",
    )

    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"


class History(models.Model):
    action = models.CharField(max_length=100, verbose_name="عملیات")
    timestamp = models.DateField(default=timezone.now, verbose_name="زمان")

    class Meta:
        verbose_name = "تاریخچه"
        verbose_name_plural = "تاریخچه‌ها"
