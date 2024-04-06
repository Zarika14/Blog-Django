from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json

from blog.models import Blog
# Create your views here.

def create_blog(request):
    try:
        
        if request.method != 'POST':

            raise Exception(f'{request.method}, Method not allowed')
        
        
        if not request.body :
    
            raise Exception('Request body Not Found')

        data = request.POST
        files = request.FILES
        
        title = data.get('title')
        # print(title)
        description = data.get('description')

        image = files.get('image')
        
        
        if not title:
            raise Exception("Title field can not be empty")
            
        
        if not description:
            raise Exception("Description field in Required")

        blog = Blog(title = title, description = description, image = image)
        blog.save()
        print(data,files)
        
        data = model_to_dict(blog)
        print(data)
        image_url = blog.image.url

        data['image'] = image_url 

        
        return JsonResponse({'message': data}, status = 200)
        
        
    except Exception as e :
        return JsonResponse({'message' : str(e)}, status = 400 )

    