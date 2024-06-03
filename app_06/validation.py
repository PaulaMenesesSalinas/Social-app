from django.core.exceptions import ValidationError

bad_words = ["cat", "dog", "fish"]


def validate_bad_words(value):
    for word in bad_words:
        if word in value.lower():
            raise ValidationError("No bad words")


def validate_email(value):
    if value and value.endswith(".what"):
        raise ValidationError("Email address should not end with '.what'.")


def validate_age(value):
    if value and (value < 18 or value > 100):
        raise ValidationError("Age should be between 18 and 100")
