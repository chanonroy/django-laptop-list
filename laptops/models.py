from django.db import models


class Manufacturer(models.Model):
    """Acer, Dell, etc."""

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class GPU(models.Model):
    """Graphics Card."""

    name = models.CharField(max_length=255)
    memory = models.IntegerField()
    benchmark = models.IntegerField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "GPUs"

    def __str__(self):
        return self.name


class CPU(models.Model):
    """CPU."""

    name = models.CharField(max_length=255)
    clock_speed_min = models.FloatField(max_length=5)
    clock_speed_max = models.FloatField(max_length=5)
    cores = models.IntegerField()
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "CPUs"

    def __str__(self):
        return self.name


class Laptop(models.Model):
    """Laptop."""

    model_name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    year = models.IntegerField()
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    gpu = models.ManyToManyField(GPU)
    weight = models.FloatField(blank=True, null=True)
    ram = models.IntegerField()
    storage = models.IntegerField()
    battery = models.FloatField(max_length=2)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model_name + ' ({})'.format(self.year)

    def GPU(self):
        return "\n".join([str(g) for g in self.gpu.all()])
