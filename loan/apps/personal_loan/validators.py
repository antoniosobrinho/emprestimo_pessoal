from django.core.validators import RegexValidator

numeric_validator = RegexValidator(
    r'^[0-9]*$',
    'Only numeric characteres are allowed'
)