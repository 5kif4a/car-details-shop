from django.db import models

# Create your models here.


class VehicleType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Mark(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class DetailType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    link_name = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    mark_id = models.ForeignKey(Mark, on_delete=models.CASCADE)
    vehicle_type_id = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    year = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{} {}'.format(self.mark_id, self.name)


class Detail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    detail_type_id = models.ForeignKey(DetailType, on_delete=models.CASCADE, null=True)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    price = models.BigIntegerField(null=True)
    img = models.ImageField(upload_to='photo', blank=True)
    description = models.TextField()

    class Meta:
        ordering = ['name', 'description']

    def __str__(self):
        return self.description


class Other(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Report(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    text = models.TextField(null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

