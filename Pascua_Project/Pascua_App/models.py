from django.db import models

# Create your models here.
class Pet(models.Model):
    record_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    visit_date = models.DateField()
    medical_notes = models.TextField()
    

    def __str__(self):
        return self.pet_name