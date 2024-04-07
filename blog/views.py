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
        
        
        if image :
            blog = Blog(title = title, description = description, image = image)
        else:
            blog = Blog(title = title, description = description)
            
        blog.save()
        # print(data,files)
        
        data = model_to_dict(blog)
        print(data)
        # image_url = blog.image.url
        # data['image'] = image_url
        if blog.image:
            data['image'] = blog.image.url 
        else:
            data['image'] = None
        
        return JsonResponse({'message': data}, status = 200)
        
        
    except Exception as e :
        return JsonResponse({'message' : str(e)}, status = 400 )

def get_particular_blog_details(request, id) : 
    try :
        if request.method != 'GET' :
            raise Exception(f'{request.method} Method not allowed')
        

        if not Blog.objects.filter(id = id).first() :
            
            raise Exception('task not found')
        
        blog = Blog.objects.get(id = id)
        data = model_to_dict(blog)
        
        
        
        # if {'image' : ' '}:
        #     raise Exception("Image field empty")
        
    
        if 'image' in data and blog.image:
            data['image'] = blog.image.url
        else:
            data['image'] = None   
            
           
            
        data['created_at'] = blog.created_at
        data['updated_at'] = blog.updated_at
            
        return JsonResponse({'blog': data}, status = 200)
    

    
    except Exception as e:
        return JsonResponse({'message' : str(e)}, status = 400)    
    
def list_all_blog(request):

    try:
        
        if request.method != 'GET':
            raise Exception(f'{request.method}, Method not allowed')
        
        blogs = Blog.objects.all()
        
        data = []
        
        for blog in blogs:
            blog_data = model_to_dict(blog)
            if 'image' in blog_data:
                blog_data['image'] = blog.image.url if blog.image else None
            data.append(blog_data)
        
        # data = [model_to_dict(task) for task in tasks]
        
        return JsonResponse({'message ': data}, status = 200)
    
    except Exception as e:
        
        return JsonResponse({'message' : str(e)}, status = 400)  
    
def delete_blog(request,id):
    try:
        if request.method != 'DELETE':
            raise Exception(f'{request.method}, Method not allowed')
        
        if not Blog.objects.filter(id = id).exists():
            raise Exception('Task does not exist')
        
        blog = Blog.objects.get(id = id)
        blog.delete()
        
        return JsonResponse({'message': "Task deleted Successfuly"},status = 200)
        
    
    except Exception as e:
        return JsonResponse({'message' : str(e)}, status = 400)


def update_blog(request, id):
    try:
        if request.method != 'POST':
            raise Exception(f'{request.method}, Method not allowed')
        
        if not Blog.objects.filter(id=id).exists():
            raise Exception("Blog does not exist")
        
        # Access form data from request.POST
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        blog = Blog.objects.get(id=id)
        
        if title:
            blog.title = title
        if description:
            blog.description = description
        if image:
            blog.image = image
        
        blog.save()
        
        # Convert the 'image' field to its URL representation
        data = model_to_dict(blog)
        
        if data['image'] : 
            data['image'] = blog.image.url
        
        return JsonResponse({'message': data}, status=200)
    
    except Exception as e:
        return JsonResponse({'message': str(e)}, status=400)