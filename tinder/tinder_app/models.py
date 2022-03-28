from django.db import models

# Create your models here.
class Member(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    firstName = models.CharField(max_length = 100, blank = True, null = True)
    lastName = models.CharField(max_length = 100, blank = True, null = True)
    email = models.EmailField()
    image = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True)

    def __str__(self):
        return '{}'.format(self.lastName + ' ' + self.firstName)

