from django.shortcuts import render
from .models import *  

def recipe_list(request):

    if request.method == 'POST':

        data = request.POST
        
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_img = request.file.get('recipe_img')
        
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_description = recipe_description,
            recipe_img = recipe_img
        )



    return render(request, 'recepi.html')  
