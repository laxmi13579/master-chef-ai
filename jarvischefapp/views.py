from django.shortcuts import render, redirect
from django.views import View
from .forms import RecipeForm
from .langchain import askJarvisChef

# Create your views here.
class Home(View):
    def get(self, request):
        ai_response_recipe = request.session.get('ai_response_recipe','')
        form = RecipeForm()
        return render(request, 'jarvischefapp/home.html', {'form': form, 'ai_response_recipe': ai_response_recipe})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data['recipe_message']
            ai_response = askJarvisChef(recipe_message)
            print('session', ai_response)
            request.session['ai_response_recipe'] = ai_response
        form = RecipeForm()
        return redirect('/')
