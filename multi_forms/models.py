from django.db import models
from model_utils import Choices

GENDER = Choices(
	("Male", "Male"),
	("Female", "Female"),
)
# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=64)
	gender = models.CharField(max_length=16, choices=GENDER, default="Male")
	age = models.CharField(max_length=3)

	def __str__(self):
		return self.name

	class Meta:
		db_table = "students"


class Marks(models.Model):
	student = models.ForeignKey(Student, related_name = "marks", on_delete=models.CASCADE)
	class_name = models.CharField(max_length=32)
	english = models.CharField(max_length=3)
	nepali = models.CharField(max_length=3)

	def __str__(self):
		return self.student

	class Meta:
		db_table = "marks"