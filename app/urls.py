from django.urls import path
from . import views
from .views import CategoryListView,CategoryCreateView,Category_create,get_category_by_id,delete_category,HomeView,BlogCreateView,Blog_create,blog_update,blog_delete
urlpatterns = [

    path('', HomeView.as_view(), name="index"),
    path('blog_create', BlogCreateView.as_view(), name = "Blog_create"),
    path('create_blog',Blog_create,name="create_blog"),
    path('blog_update/<int:id>',blog_update,name="blog_update"),
    path('delete_blog<int:id>',blog_delete, name="deleteblog"),
    # view list all category
    path('category',CategoryListView.as_view(), name="category_list"),
    # end view 
    # View - Create category
    path('create_category',CategoryCreateView.as_view(), name="create_category"),
    path('category_create',Category_create,name="category_create_post"),
    # End 

    # View - Upate category
    path('category/<int:id>',get_category_by_id, name="update_category"),
    # End

    # Delete category
    path('delete_category<int:id>',delete_category, name="deletecategory"),
    # end

]

