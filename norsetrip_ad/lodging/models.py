from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Lodging(models.Model):
	lodge_id = models.AutoField(primary_key = True, db_column = "LodgeId");#auto incrementing
 	lodge_name = models.CharField(max_length = 200)
 	#course_Id = models.ForeignKey(Course,verbose_name = "course_id")
 	lodge_address = models.CharField(max_length = 200, db_column = "Address")
 	city = models.CharField(max_length = 100, db_column = "City")
 	country = models.CharField(max_length = 100, db_column = "Country")
 	lodge_phone = models.IntegerField(db_column = "Phone")
 	lodge_email = models.EmailField(db_column = "Email")
 	lodge_description = models.TextField(db.column = "Description")



