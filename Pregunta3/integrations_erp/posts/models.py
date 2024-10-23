from django.db import models

class DimAddresses(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    geo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}"

class DimCompanies(models.Model):
    name = models.CharField(max_length=100)
    catchPhrase = models.CharField(max_length=100)
    bs = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class DimUsers(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    address = models.OneToOneField(DimAddresses, on_delete=models.CASCADE)
    company = models.OneToOneField(DimCompanies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class DimPosts(models.Model):
    userId = models.IntegerField(null=False)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

class FactPosts(models.Model):
    users = models.ForeignKey(DimUsers, on_delete=models.CASCADE, related_name='users')
    posts = models.ForeignKey(DimPosts, on_delete=models.CASCADE, related_name='posts')
