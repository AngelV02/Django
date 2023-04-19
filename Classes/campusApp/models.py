from django.db import models

# Create your models here.

from django.db import models


# This class defines the UniversityCampus model
class UniversityCampus(models.Model):
    # These are the attributes of the UniversityCampus model
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    campus_id = models.IntegerField()

    # This is the Model Manager for the UniversityCampus model
    objects = models.Manager()

    # This Meta class specifies how the model should be displayed on the admin page
    def __str__(self):
        return self.name

    # This method returns a string representation of the UniversityCampus object
    class Meta:
        verbose_name_plural = "University Campuses"
