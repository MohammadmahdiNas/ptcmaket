from rest_framework import serializers

from ..models import Contact, Apply, Order


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'description', 'created_at']
        read_only_fields = ['id', 'created_at']


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields = ["id", "first_name", "last_name", "study_field", "email", "phone_number", "education_degree", "resume",
                  "cover_letter", "status", "created_at"]
        read_only_fields = ["id", "created_at", "status"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "company_name", "activity_area", "email", "contact_number", "explanation", "status",
                  "created_at"]
        read_only_fields = ["id", "created_at", "status"]