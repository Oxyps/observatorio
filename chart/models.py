from django.db import models

class Granularity(models.Model):
	granularity = models.CharField(max_length=20)

class ReferencePeriod(models.Model):
	in_date = models.DateField()
	until_date = models.DateField()

class Location(models.Model):
	id_ibge = models.PositiveIntegerField(primary_key=True)
	id_ibge_memberof = models.PositiveIntegerField()
	name = models.CharField(max_length=45)
	nickname = models.CharField(max_length=10)
	location_type = models.CharField(max_length=45)
	geo_latitude = models.FloatField()
	geo_longitude = models.FloatField()

class DataType(models.Model):
	datatype = models.CharField(max_length=20)

class Information(models.Model):
	nickname = models.CharField(max_length=15)
	shortname = models.CharField(max_length=100)
	longname = models.CharField(max_length=256)
	definition = models.TextField(max_length=2048)
	id_datatype = models.OneToOneField('DataType', on_delete=models.DO_NOTHING, unique=True, db_column='id_datatype')

class Data(models.Model):
	class Meta:
		unique_together = (('id_information', 'id_information_datatype', 'id_reference_period', 'id_location', 'id_granularity'),)

	id_information = models.ForeignKey('Information', on_delete=models.DO_NOTHING, db_column='id_information')
	id_information_datatype = models.ForeignKey('Information', on_delete=models.DO_NOTHING, to_field='id_datatype', related_name='information_datatype', db_column='id_information_datatype')
	id_reference_period = models.ForeignKey('ReferencePeriod', on_delete=models.DO_NOTHING, db_column='id_reference_period')
	id_location = models.ForeignKey('Location', on_delete=models.DO_NOTHING, db_column='id_location')
	id_granularity = models.ForeignKey('Granularity', on_delete=models.DO_NOTHING, db_column='id_granularity')
	data = models.FloatField()
