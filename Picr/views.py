# Create your views here.

from django.shortcuts import render_to_response, render
import time, uuid, os, datetime

from Picr.models import Image

import urllib2

def home(request):
	return render_to_response('Picr/index.html')

def submitted(request):
	if request.GET['image'] == '':
		return render_to_response('Picr/error.html')
	else:
		image = request.GET['image']

	if request.GET['tags'] == '':
		tags = ''
	else:
		tags = request.GET['tags']

	
	 

#Save the image to a folder
	
	#Get the file extension
	filename_extension = image.split('.')[-1]
	#Give the file a UUID for a filename. In theory there should not be a name collision. 
	local_filename = str(uuid.uuid4())

	#Download the image itself
	remote_file = urllib2.urlopen(image)
	#Open up a local file
	#!!!!Need to figure out how to save to a static directory!!!!!
	local_file = open(str(os.getcwd()) + "/Picr/Images/" + local_filename + "." + filename_extension, "w" )
	#Write the image to the local file
	local_file.write(remote_file.read())
	#Close out the file
	local_file.close()

#Save the tags, filename, and upload time to the database
	
	database_entry = Image(image_filename=local_filename + "." + filename_extension,image_tags=tags,image_upload_date=datetime.datetime.now())
	database_entry.save()



	context = {'image' : image, 'tags' : tags, 'local_filename': local_filename, 'filename_extension' : filename_extension }
	return render_to_response('Picr/submitted.html', context)


def gallery(request):
	return render_to_response('Picr/gallery.html')