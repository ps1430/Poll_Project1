from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db import models

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_four=models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    option_four_count=models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
    def __str__(self):
        return self.question
class UserProfile(models.Model):
    question=models.ForeignKey(Poll,on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='User Profile'