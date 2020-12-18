from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
#Django fields : https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types

class Post(models.Model):#defining our model(it is an object) and Post is our model name
    #models.Model means that the post is a django model. so Django knows that it should be saved in the database
    # defining properties: title,text,created _date,published_date and author.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title








