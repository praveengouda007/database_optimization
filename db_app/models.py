from django.db import models

# Create your models here.
class A(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class B(models.Model):
    name = models.CharField(max_length=30)
    a = models.ForeignKey(A, related_name="b", on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s'%(self.name, self.a)

class C(models.Model):
    a = models.ManyToManyField(A, related_name='c')
    name = models.CharField(max_length=30)
    # num = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s'%(self.name, self.a)