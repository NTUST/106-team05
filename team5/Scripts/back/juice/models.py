from django.db import models


class Member(models.Model):
	Member_id = models.CharField(max_length=200)
	Member_name = models.CharField(max_length=200)
	Member_email = models.CharField(max_length=200)
	Member_password = models.CharField(max_length=200)
	Member_phone = models.CharField(max_length=200)
	Member_address = models.CharField(max_length=200)

	def __str__(self):
		return self.Member_name


class Food(models.Model):
	Food_id = models.CharField(max_length=200)
	Food_name = models.CharField(max_length=200)
	Food_cost = models.IntegerField(default=0)
	Food_amount = models.IntegerField(default=0)
	Food_season = models.CharField(max_length=200)

	def __str__(self):
		return self.Food_name

class List(models.Model):
	List_id = models.CharField(max_length=200)
	customer = models.ForeignKey(Member, on_delete=models.CASCADE)
	List_time = models.DateTimeField('date published')
	List_content = models.CharField(max_length=200)

	def __str__(self):
		return self.List_id + "  " + str(self.List_time)