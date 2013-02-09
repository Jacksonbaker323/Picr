from django.db import models

class Image(models.Model):
	#Filename of the image (UUID4)
	image_filename = models.CharField(max_length=1000)
	#User submitted tags
	image_tags = models.CharField(max_length=1000)
	#Date that the image was uploaded
	image_upload_date = models.DateTimeField()
	def __unicode__(self):
		return self.image_filename