"""Utils: Validators."""

from django.core.exceptions import ValidationError


def validate_extension(value):
    """
    Validates that the uploaded file has a '.webp' or '.svg' extension,
    and the file size is not greater than 1MB
    """
    valid_extensions = ["webp", "svg", "jpg"]
    max_size_mb = 1
    extension = value.name.split(".")[-1]

    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError("File size should not exceed 1MB.")

    if not extension in valid_extensions:
        raise ValidationError("Only .webp and .svg files are allowed.")
