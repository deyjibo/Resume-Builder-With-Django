from django.db import models


class Profile(models.Model):
    id = models.BigAutoField(
        auto_created=True, serialize=False, primary_key=True, verbose_name='ID')
    Name = models.CharField(max_length=20, default='')
    phone = models.CharField(max_length=10, default='')
    add = models.CharField(max_length=50, default='')
    dob = models.CharField(max_length=10, default='')
    gen = models.CharField(max_length=50, default='')
    lang = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    university = models.CharField(max_length=20, default='')
    course = models.CharField(max_length=20, default='')
    year = models.CharField(max_length=20, default='')
    perc = models.CharField(max_length=20, default='')
    college = models.CharField(max_length=20, default='')
    course1 = models.CharField(max_length=20, default='')
    year1 = models.CharField(max_length=20, default='')
    perc1 = models.CharField(max_length=20, default='')
    skills = models.TextField(max_length=20, default='')
    career = models.TextField(max_length=400, default='')
    strength = models.TextField(max_length=200, default='')
    area = models.CharField(max_length=200, default='')

    class Meta:
        db_table='Profile'

