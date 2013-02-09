# Imports
import os
from django.shortcuts import render_to_response, render
from Picr.models import Image
from Picr.custom_objects import image_obj
import urllib2
import uuid
import datetime


#Main page
def home(request):
	return render_to_response('Picr/index.html')


#Submitted image page
def submitted(request):
	
	#Get the information from the submission
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
	local_file = open(str(os.getcwd()) + "/Picr/Images/" + local_filename + "." + filename_extension, "w" )
	#Write the image to the local file
	local_file.write(remote_file.read())
	#Close out the file
	local_file.close()
#Save the tags, filename, and upload time to the database
	database_entry = Image(image_filename=local_filename + "." + filename_extension,image_tags=tags,image_upload_date=datetime.datetime.now())
	database_entry.save()

#Get the data for the page
	context = {'image' : image, 'tags' : tags, 'local_filename': local_filename, 'filename_extension' : filename_extension }
	return render_to_response('Picr/submitted.html', context)

#Gallery page
def gallery(request):
	
	#Create a dictionary to hold the gallery images
	gallery_dict = []
	#List all of the images
	list = Image.objects.all()

	#Iterate through the list, get the image information, make an object with it and then append it to a dictionary.
	for x in list:
		item = image_obj(x.image_filename, x.image_tags, x.image_upload_date)
		gallery_dict.append(item)

#Get the data for the page
	context = {'gallery_dict' : gallery_dict}
	return render_to_response('Picr/gallery.html', context)

#Search results page
def search(request):
	#Get the information from the page
	if request.GET['search'] == '':
		context = {'error' : "No search tags submitted"}
		return render_to_response('Picr/search.html', context)
	else:
		tags = request.GET['search']
		tags = tags.split(" ")
		search_results = []
		#Get the individual tag in the list of tags that the user submitted
		for tag in tags:
			#Check to see if any image contains that tags
			list = Image.objects.filter(image_tags__contains=tag)
			for item in list:
				#Check to see if that image is already in the list
				x = image_obj(item.image_filename, item.image_tags, item.image_upload_date)
				#If it is in the list tlthen leave it out
				if search_results.count(x) >= 1:
					break
				#Otherwise add it to the search_results list
				else:
					search_results.append(x)
		
		
		
#Get the data for the page
		context = {'tags' : tags, 'search_results' : search_results}
		return render_to_response('Picr/search.html', context)
