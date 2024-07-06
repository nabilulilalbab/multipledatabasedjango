from django.db import models

# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()

    def __str__(self) -> str:
        return self.judul