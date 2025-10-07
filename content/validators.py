from django.core.exceptions import ValidationError

def validate_file_size(file):
    max_size = 150
    if file.size > max_size * 1024:
        raise ValidationError(f'File can not be larger than {max_size} kb')