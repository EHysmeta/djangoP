from django.db import models

# Create your models here.

class category(models.Model):
    category_name = models.CharField(max_length=60,null=True, blank=True)
    category_image = models.ImageField(upload_to='category/',null=True, blank=True)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_title = models.CharField(max_length=250, null=True, blank=True)
    item_description = models.TextField(max_length=9000, null=True, blank=True)
    item_image = models.ImageField(upload_to='item/', null=True, blank=True)
    item_category = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.item_title}'
    
class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=60,null=True, blank=True)
    staff_mbiemri = models.CharField(max_length=60, null=True, blank=True)
    staff_image = models.ImageField(upload_to='staff/',null=True, blank=True)
    staff_description = models.TextField(max_length=9000, null=True, blank=True)
    staff_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'{self.staff_name} {self.staff_mbiemri}'
    
class Contact(models.Model):
    contact_name = models.CharField(max_length=60,null=True, blank=True)
    contact_mbiemri = models.CharField(max_length=60, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    scontac_sms = models.TextField(max_length=9000, null=True, blank=True)

    def __str__(self):
        return f'{self.contact_name} {self.contact_mbiemri}'
    