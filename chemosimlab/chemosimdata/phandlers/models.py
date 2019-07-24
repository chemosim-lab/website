from django.db import models

# Create your models here.
class Ligend(models.Model):
	inchikey=models.CharField(max_length=255)
	name= models.CharField(max_length=255)
	smiles= models.CharField(max_length=255)
	def __str__(self):
		return self.name
class Recepteur(models.Model):
	uniprot_id=models.CharField(max_length=255)
	name= models.CharField(max_length=255)
	sequence= models.CharField(max_length=1000)
	espece=models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Donnee_affinite(models.Model):
	id_legend= models.ForeignKey(Ligend, on_delete=models.CASCADE)
	id_recepteur= models.ForeignKey(Recepteur, on_delete=models.CASCADE)
	EC50=models.FloatField(null=True, blank=True, default=None)
	ref=models.CharField(max_length=255)
	
	def __str__(self):
		return self.EC50



