from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

def validate_resume_file(file):
    valid_mime_types = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']
    file_mime_type = file.content_type
    if file_mime_type not in valid_mime_types:
        raise ValidationError(_('Unsupported file type. Only PDF and Word documents are allowed.'))
    max_size = 400  # 400 KB
    if file.size > max_size * 1024:
        raise ValidationError(_(f'File size exceeds the limit of {max_size} KB.'))
    return file