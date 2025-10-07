from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Apply(models.Model):
    STATUS_CHOICES = [
        (
            "pending",
            "pending",
        ),  # first is name in database seccond is name for display in admin or site
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    education_degree = models.CharField(max_length=30)
    study_field = models.CharField(max_length=30)
    resume = models.FileField(upload_to="resumes/")
    cover_letter = models.TextField()
    status = models.CharField(
        max_length=10,  # ex rejected
        choices=STATUS_CHOICES,
        default="pending",
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    company_name = models.CharField(max_length=50)
    activity_area = models.CharField(max_length=50)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("pending", "pending"),
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]
    status = models.CharField(
        max_length=10,  # ex rejected
        choices=STATUS_CHOICES,
        default="pending",
    )
