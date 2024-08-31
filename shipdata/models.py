from django.db import models
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value <= 0:
        raise ValidationError('This value must be positive.')

class ParameterSubmission(models.Model):
    wd_min = models.CharField(max_length=255)
    wwl = models.CharField(max_length=255)
    lwl = models.CharField(max_length=255)
    wvpi = models.CharField( max_length=255)
    ukc = models.CharField(max_length=255)
    dx_min = models.CharField(max_length=255)
    blend = models.CharField(max_length=255)
    nl_c = models.CharField(max_length=255)
    nl_m = models.CharField(max_length=255)

    def __str__(self):
        return f"Submission {self.id} - {self.wd_min}, {self.wwl}, {self.lwl}"

    def clean(self):
        # Add any cross-field validation here if needed
        pass