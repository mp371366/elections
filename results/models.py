from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return "{self.name} {self.surname}"

class Voivodeship(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Województwo {self.name}"

class District(models.Model):
    name = models.CharField(max_length=40)
    voivodeship = models.ForeignKey(Voivodeship, on_delete=models.CASCADE)

    def __str__(self):
        return "Powiat {self.name}"

class Unit(models.Model):
    name = models.CharField(max_length=40)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return "Gmina {self.name}"

class Result(models.Model):
    result = models.PositiveIntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return "{self.result}"
