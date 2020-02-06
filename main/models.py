from django.db import models

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    article_header = models.CharField(max_length=250)
    article_body = models.TextField()

    def __str__(self):
        return self.article_header