from django.shortcuts import render
from django.conf import settings
import os
import json
data = os.path.join( settings.BASE_DIR, 'collaborate/data' )

testimonial_json = open(data+'/testimonial.json','r').read()
home_json = open(data+'/home.json','r').read()
course_json = open(data+'/course.json','r').read()
place_json = open(data+'/placetolearn.json','r').read()


def home(request):
    testimonial_data = json.loads(testimonial_json)
    home_data = json.loads(home_json)
    course_data = json.loads(course_json)
    place_data = json.loads(place_json)
    return render(request,'home.html',
        {
        "course_data" : course_data,
        "testimonial_data" : testimonial_data,
        "home_data" : home_data,
        "place_data" : place_data
        })