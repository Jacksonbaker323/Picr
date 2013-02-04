from django.db import models

class Image(models.Model):
	image_filename = models.CharField(max_length=1000)
	image_tags = models.CharField(max_length=1000)
	image_upload_date = models.DateTimeField()
	def __unicode__(self):
		return self.image_filename