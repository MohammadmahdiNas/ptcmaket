from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import validate_resume_file


class Contact(models.Model):
    first_name = models.CharField(max_length=50, verbose_name=_("نام"))
    last_name = models.CharField(max_length=50, verbose_name=_("نام خانوادگی"))
    email = models.EmailField(verbose_name=_("ایمیل"))
    phone_number = models.CharField(max_length=15, verbose_name=_("شماره تماس"))
    description = models.TextField(verbose_name=_("توضیحات"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))

    class Meta:
        verbose_name = _("ارتباط")
        verbose_name_plural = _("ارتباطات")


class Apply(models.Model):
    STATUS_CHOICES = [
        (
            "pending",
            _("در انتظار"),
        ),  # first is name in database seccond is name for display in admin or site
        ("accepted", _("پذیرفته شده")),
        ("rejected", _("رد شده")),
    ]

    first_name = models.CharField(max_length=50, verbose_name=_("نام"))
    last_name = models.CharField(max_length=50, verbose_name=_("نام خانوادگی"))
    email = models.EmailField(verbose_name=_("ایمیل"))
    phone_number = models.CharField(max_length=15, verbose_name=_("شماره تماس"))
    education_degree = models.CharField(max_length=30, verbose_name=_("مقطع تحصیلی"))
    study_field = models.CharField(max_length=30, verbose_name=_("رشته تحصیلی"))
    resume = models.FileField(upload_to="resumes/", validators=[validate_resume_file], verbose_name=_("رزومه"))
    cover_letter = models.TextField(verbose_name=_("نامه پیوست"))
    status = models.CharField(
        max_length=10,  # ex rejected
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name=_("وضعیت"),
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد"))

    class Meta:
        verbose_name = _("درخواست")
        verbose_name_plural = _("درخواست‌ها")    


class Order(models.Model):
    company_name = models.CharField(max_length=50, verbose_name=_("نام شرکت"))
    activity_area = models.CharField(max_length=50, verbose_name=_("حوزه فعالیت"))
    email = models.EmailField(verbose_name=_("ایمیل"))
    contact_number = models.CharField(max_length=15, verbose_name=_("شماره تماس"))
    explanation = models.TextField(verbose_name=_("توضیحات"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("تاریخ ایجاد")) 

    STATUS_CHOICES = [
        ("pending", _("در انتظار")),
        ("accepted", _("پذیرفته شده")),
        ("rejected", _("رد شده")),
    ]
    status = models.CharField(
        max_length=10,  # ex rejected
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name=_("وضعیت"),
    )

    class Meta:
        verbose_name = _("سفارش")
        verbose_name_plural = _("سفارش‌ها")


class History(models.Model):
    action = models.CharField(max_length=100, verbose_name=_("عملیات"))
    timestamp = models.DateField(default=timezone.now, verbose_name=_("زمان"))

    class Meta:
        verbose_name = _("تاریخچه")
        verbose_name_plural = _("تاریخچه‌ها")
