from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView,DetailView
from .models import *

# Create your views here.

class HomeView(TemplateView):
    template_name = "apps/home.html"

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        list_all_blog = Blog.objects.all()
        list_all_category = Category.objects.all()
        context = {'list_all_blog' : list_all_blog, 'list_all_category' :list_all_category}
        return context
        

class BlogCreateView(TemplateView):
    template_name = "apps/blogs/blog_create.html"

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        list_all_category = Category.objects.all()
        context['list_all_category'] = list_all_category
        return context


def Blog_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        content = request.POST.get('content')
        cat = request.POST.get('cat')
        Blog.objects.create(
            name = name,
            content = content,
            category_id = cat
        )
        return redirect('/')

def blog_update(request, id):
    blog = Blog.objects.get(pk=id)
    category = Category.objects.all()
    
    if request.method =="POST":
        blog.name = request.POST['blog_name']
        blog.content = request.POST['blog_content']
        blog.category_id = request.POST['blog_cat']
        blog.save()
        return redirect('/')
    return render(request, 'apps/blogs/blog_update.html', {'blog': blog,'category': category })

def blog_delete (request , id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('/')

class CategoryListView(TemplateView):
    template_name ="apps/category/category_view.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        list_all_category = Category.objects.all()
        context['list_all_category'] = list_all_category
        return context

class CategoryCreateView(TemplateView):
    template_name ="apps/category/category_create.html"

def Category_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('/category')
def get_category_by_id(request, id):
    category = Category.objects.get(pk=id)
    
    if request.method =="POST":
        category.name = request.POST['cat_name']
        category.save()
        return redirect('/category')
    return render(request, 'apps/category/category_update.html', {'category': category})

def delete_category(request,id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('/category')
